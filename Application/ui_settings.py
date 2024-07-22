import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import os

class AddTrustedUserDialog(simpledialog.Dialog):
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

        # Here you can add code to save the trusted user's info
        # For now, just print it
        print(f"Trusted User Added: {self.name}, {self.phone}, {self.email}")
        messagebox.showinfo("Info", "Trusted user added successfully!")

class SettingsScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Settings")
        self.root.geometry("400x500")

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("TCheckbutton", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
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

        self.app_status = tk.BooleanVar(value=True)
        app_toggle_label = ttk.Label(general_inner_frame, text="Turn App On/Off", background="#2C3E50", foreground="#4CAF50")
        app_toggle_label.pack(anchor="w", padx=10, pady=5)
        app_toggle_button = ttk.Checkbutton(general_inner_frame, text="On/Off", variable=self.app_status, style="TCheckbutton")
        app_toggle_button.pack(anchor="w", padx=10, pady=5)

        notifications_var = tk.BooleanVar(value=True)
        notifications_check = ttk.Checkbutton(general_inner_frame, text="Enable Notifications", variable=notifications_var, style="TCheckbutton")
        notifications_check.pack(anchor="w", padx=10, pady=5)

        add_trusted_user_button = ttk.Button(general_inner_frame, text="Add Trusted User", command=self.add_trusted_user)
        add_trusted_user_button.pack(anchor="w", padx=10, pady=5)

        # Account Settings
        account_settings_frame = ttk.LabelFrame(root, text="Account Settings", style="TLabelframe")
        account_settings_frame.pack(pady=10, padx=10, fill="x")

        account_inner_frame = tk.Frame(account_settings_frame, bg="#2C3E50")
        account_inner_frame.pack(fill="x")

        change_password_button = ttk.Button(account_inner_frame, text="Change Password")
        change_password_button.pack(padx=10, pady=10)

        # Privacy Policy
        privacy_policy_frame = ttk.LabelFrame(root, text="Privacy Policy", style="TLabelframe")
        privacy_policy_frame.pack(pady=10, padx=10, fill="x")

        privacy_policy_inner_frame = tk.Frame(privacy_policy_frame, bg="#2C3E50")
        privacy_policy_inner_frame.pack(fill="x")

        # Placeholder for privacy policy content
        privacy_policy_content = tk.Label(privacy_policy_inner_frame, text="", bg="#2C3E50", fg="#4CAF50", font=("Helvetica", 12))
        privacy_policy_content.pack(padx=10, pady=10)

        # Back to Main Screen Button
        back_button = ttk.Button(root, text="Back to Main Screen", command=self.back_to_main)
        back_button.pack(side="bottom", anchor="w", padx=10, pady=10)

        # Logout Button
        logout_button = ttk.Button(root, text="Logout", command=self.logout)
        logout_button.pack(side="bottom", anchor="e", padx=10, pady=10)

    def add_trusted_user(self):
        AddTrustedUserDialog(self.root)

    def back_to_main(self):
        # Function to go back to main screen
        self.root.destroy()
        os.system("python ui_design.py")

    def logout(self):
        # Logout functionality
        print("Logging out")
        # Implement actual logout logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsScreen(root)
    root.mainloop()
