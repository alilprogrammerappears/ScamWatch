import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

class SettingsScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Settings")
        self.root.geometry("400x500")
        
        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#FFFFFF", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("TCheckbutton", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))

        # Background
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="Settings", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.pack(pady=10)

        # App Toggle Button
        self.app_status = tk.BooleanVar(value=True)
        app_toggle_frame = tk.Frame(root, bg="#2C3E50")
        app_toggle_frame.pack(pady=10, fill="x")
        app_toggle_label = ttk.Label(app_toggle_frame, text="Turn App On/Off", background="#2C3E50", foreground="#4CAF50")
        app_toggle_label.pack(side="left", padx=10)
        app_toggle_button = ttk.Checkbutton(app_toggle_frame, text="On/Off", variable=self.app_status, style="TCheckbutton")
        app_toggle_button.pack(side="right", padx=10)

        # General Settings
        general_settings_frame = tk.LabelFrame(root, text="General Settings", bg="#2C3E50", fg="#4CAF50", font=("Helvetica", 14, "bold"))
        general_settings_frame.pack(pady=10, padx=10, fill="x")
        
        dark_mode_var = tk.BooleanVar(value=False)
        dark_mode_check = ttk.Checkbutton(general_settings_frame, text="Enable Dark Mode", variable=dark_mode_var, style="TCheckbutton")
        dark_mode_check.pack(anchor="w", padx=10, pady=5)

        notifications_var = tk.BooleanVar(value=True)
        notifications_check = ttk.Checkbutton(general_settings_frame, text="Enable Notifications", variable=notifications_var, style="TCheckbutton")
        notifications_check.pack(anchor="w", padx=10, pady=5)

        # Account Settings
        account_settings_frame = tk.LabelFrame(root, text="Account Settings", bg="#2C3E50", fg="#4CAF50", font=("Helvetica", 14, "bold"))
        account_settings_frame.pack(pady=10, padx=10, fill="x")

        email_label = ttk.Label(account_settings_frame, text="Email:", background="#2C3E50", foreground="#4CAF50")
        email_label.pack(anchor="w", padx=10, pady=5)
        email_entry = ttk.Entry(account_settings_frame, width=30)
        email_entry.pack(padx=10, pady=5)

        password_label = ttk.Label(account_settings_frame, text="Password:", background="#2C3E50", foreground="#4CAF50")
        password_label.pack(anchor="w", padx=10, pady=5)
        password_entry = ttk.Entry(account_settings_frame, width=30, show="*")
        password_entry.pack(padx=10, pady=5)

        # Logout Button
        logout_button = ttk.Button(root, text="Logout", command=self.logout)
        logout_button.pack(side="bottom", anchor="e", padx=10, pady=10)

    def logout(self):
        # Logout functionality
        print("Logging out")
        # Implement actual logout logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsScreen(root)
    root.mainloop()
