import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import mysql.connector
import os
import subprocess
from process_blocking import one_time_connection
import logging
from dbconnect import get_trusted_emails

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

logging.getLogger('PIL').setLevel(logging.WARNING)

class AddTrustedUserDialog(simpledialog.Dialog):
    def __init__(self, parent, current_user_id):
        self.current_user_id = current_user_id
        super().__init__(parent)
        
    def body(self, master):
        self.title("Add Trusted User")

        ttk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = ttk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(master, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = ttk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(master, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = ttk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        return self.name_entry  # initial focus

    def apply(self):
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.email = self.email_entry.get()

        # Connect to the database and insert the trusted user information
        try:
            connection = mysql.connector.connect(
                host="swatch.cvuie4ieiptg.us-east-2.rds.amazonaws.com",
                user="admin",
                password="scamwatch",
                database="scamwatch_users"
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO trustedusers (user_id, name, phonenumber, email) VALUES (%s, %s, %s, %s)",
                (self.current_user_id, self.name, self.phone, self.email)
            )
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Info", "Trusted user added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error adding trusted user: {err}")
            logging.error(f"Error adding trusted user: {err}")

class SettingsScreen:
    def __init__(self, root, current_user_id):
        self.root = root
        self.current_user_id = current_user_id
        self.root.title("ScamWatch Settings")
        self.root.geometry("500x700")

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("TFrame", background="#2C3E50")
        self.style.configure("TLabelframe", background="#2C3E50")
        self.style.configure("TLabelframe.Label", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 14, "bold"))

        # Background
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="Settings", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.pack(pady=10)

        # General Settings
        general_settings_frame = ttk.LabelFrame(root, text="General Settings", style="TLabelframe")
        general_settings_frame.pack(pady=10, padx=10, fill="x")

        general_inner_frame = tk.Frame(general_settings_frame, bg="#2C3E50")
        general_inner_frame.pack(fill="x")

        add_trusted_user_button = ttk.Button(general_inner_frame, text="Add Trusted User", command=self.add_trusted_user)
        add_trusted_user_button.pack(padx=10, pady=5)

        show_trusted_users_button = ttk.Button(general_inner_frame, text="Show Trusted Users", command=self.show_trusted_users)
        show_trusted_users_button.pack(padx=10, pady=5)

        one_time_connection_button = ttk.Button(general_inner_frame, text="One-Time Connection", command=self.one_time_connection)
        one_time_connection_button.pack(padx=10, pady=5)

        # Account Settings
        account_settings_frame = ttk.LabelFrame(root, text="Account Settings", style="TLabelframe")
        account_settings_frame.pack(pady=10, padx=10, fill="x")

        account_inner_frame = tk.Frame(account_settings_frame, bg="#2C3E50")
        account_inner_frame.pack(fill="x")

        change_password_button = ttk.Button(account_inner_frame, text="Change Password (BETA)", command=self.change_password)
        change_password_button.pack(padx=10, pady=10)

        # Privacy Policy
        privacy_policy_frame = ttk.LabelFrame(root, text="Privacy Policy", style="TLabelframe")
        privacy_policy_frame.pack(pady=10, padx=10, fill="x")

        privacy_policy_inner_frame = tk.Frame(privacy_policy_frame, bg="#2C3E50")
        privacy_policy_inner_frame.pack(fill="x")

        privacy_policy_content = tk.Text(privacy_policy_inner_frame, height=10, wrap="word", bg="#2C3E50", fg="#4CAF50", font=("Helvetica", 12))
        privacy_policy_content.insert(tk.END, "Scamwatch serves to protect you against potential scammers trying to access your system via remote computer connection apps.\n\nWe value your privacy and protect your personal information.\n\nOur policies are designed to safeguard your data and maintain your trust.")
        privacy_policy_content.pack(padx=10, pady=10)
        privacy_policy_content.config(state=tk.DISABLED)  # Make the text read-only

        # Logout Button
        logout_button = ttk.Button(root, text="Logout", command=self.logout)
        logout_button.pack(side="bottom", anchor="e", padx=10, pady=10)

    def add_trusted_user(self):
        AddTrustedUserDialog(self.root, self.current_user_id)

    def show_trusted_users(self):
        # Fetch trusted users from the database and display them in a new window
        trusted_users_window = tk.Toplevel(self.root)
        trusted_users_window.title("Trusted Users")
        trusted_users_window.geometry("400x300")
        trusted_users_window.configure(bg="#2C3E50")

        trusted_users_title = tk.Label(trusted_users_window, text="Trusted Users", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#4CAF50")
        trusted_users_title.pack(pady=10)

        try:
            connection = mysql.connector.connect(
                host="swatch.cvuie4ieiptg.us-east-2.rds.amazonaws.com",
                user="admin",
                password="scamwatch",
                database="scamwatch_users"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT name, phonenumber, email FROM trustedusers WHERE user_id = %s", (self.current_user_id,))
            trusted_users = cursor.fetchall()
            cursor.close()
            connection.close()

            for user in trusted_users:
                user_label = tk.Label(trusted_users_window, text=f"Name: {user[0]}, Phone: {user[1]}, Email: {user[2]}", font=("Helvetica", 12), bg="#2C3E50", fg="#FFFFFF")
                user_label.pack(pady=5)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching trusted users: {err}")
            logging.error(f"Error fetching trusted users: {err}")

    def logout(self):
        self.root.destroy()
        script_path = os.path.join(os.path.dirname(__file__), 'ui_login.py')
        subprocess.Popen(["python", script_path])

    def change_password(self):
        messagebox.showinfo("Info", "Change Password feature is under development.")

    def one_time_connection(self):
        try:
            one_time_connection()
        except Exception as e:
            logging.error(f"Error calling one_time_connection: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    current_user_id = 1  # Replace with actual user ID obtained after login
    app = SettingsScreen(root, current_user_id=current_user_id)
    root.mainloop()
