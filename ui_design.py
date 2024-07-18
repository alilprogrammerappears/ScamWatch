import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw
import subprocess

# Placeholder for the current user 
current_user = "JohnDoe"

class ScamWatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch")
        self.root.geometry("900x700")  # Adjusted window size to fit all elements

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#2C3E50", foreground="#FFFFFF", font=("Helvetica", 12))
        self.style.configure("TFrame", background="#2C3E50")
        
        # Background
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="ScamWatch", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        # Load and display image
        self.logo_image = Image.open("login bg.png")
        self.logo_image = self.logo_image.resize((100, 100), Image.LANCZOS)

        # Create a circular mask
        mask = Image.new("L", self.logo_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + self.logo_image.size, fill=255)
        self.logo_image.putalpha(mask)

        # Apply mask to make image circular
        self.logo_image = ImageOps.fit(self.logo_image, mask.size, centering=(0.5, 0.5))
        self.logo_image.putalpha(mask)

        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        logo_label = tk.Label(root, image=self.logo_photo, bg="#2C3E50")
        logo_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Username and Settings
        button_frame = tk.Frame(root, bg="#2C3E50")
        button_frame.grid(row=0, column=2, rowspan=2, columnspan=3, padx=20, pady=10, sticky="ne")
        
        username_button = ttk.Button(button_frame, text=f"User Name: {current_user}", command=self.show_profile)
        username_button.pack(pady=5)
        
        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(pady=5)
        
        one_time_connection_button = ttk.Button(button_frame, text="One-Time Connection", command=self.one_time_connection)
        one_time_connection_button.pack(pady=5)

        learn_more_button = ttk.Button(button_frame, text="Learn More", command=self.open_learn_more)
        learn_more_button.pack(pady=5)

        logout_button = ttk.Button(button_frame, text="Log Out", command=self.log_out)
        logout_button.pack(pady=5)

        # Summary
        summary_label = tk.Label(root, text="Summary of recent scam alerts or notifications", bg="#2C3E50", fg="#4CAF50")
        summary_label.grid(row=2, column=0, columnspan=2, pady=5)
        summary_text = tk.Text(root, height=10, width=50)
        summary_text.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="e")

        # Statistics
        stats_frame = tk.Frame(root, bg="#2C3E50", padx=10, pady=10)
        stats_frame.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        stats_label = tk.Label(stats_frame, text="Statistics", bg="#2C3E50", fg="#4CAF50", font=("Helvetica", 16))
        stats_label.grid(row=0, column=0, columnspan=2, pady=5)
        
        detected_label = tk.Label(stats_frame, text="Number of Scams detected", bg="#2C3E50", fg="#4CAF50")
        detected_label.grid(row=1, column=0, sticky="w")
        detected_value = tk.Label(stats_frame, text="0", bg="white", fg="#2C3E50", width=10)
        detected_value.grid(row=1, column=1, sticky="e")
        
        prevented_label = tk.Label(stats_frame, text="Number of Scams prevented", bg="#2C3E50", fg="#4CAF50")
        prevented_label.grid(row=2, column=0, sticky="w")
        prevented_value = tk.Label(stats_frame, text="0", bg="white", fg="#2C3E50", width=10)
        prevented_value.grid(row=2, column=1, sticky="e")

    def show_profile(self):
        # Functionality to show user profile
        profile_window = tk.Toplevel(self.root)
        profile_window.title("User Profile")
        profile_window.geometry("400x300")
        profile_window.configure(bg="#2C3E50")
        
        profile_title = tk.Label(profile_window, text="User Profile", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#4CAF50")
        profile_title.pack(pady=10)
        
        username_label = tk.Label(profile_window, text=f"Username: {current_user}", font=("Helvetica", 14), bg="#2C3E50", fg="#FFFFFF")
        username_label.pack(pady=5)
        
        # Add more profile details here
        email_label = tk.Label(profile_window, text="Email: johndoe@example.com", font=("Helvetica", 14), bg="#2C3E50", fg="#FFFFFF")
        email_label.pack(pady=5)
        
        # Add more fields as needed
        # ...
        
        close_button = ttk.Button(profile_window, text="Close", command=profile_window.destroy)
        close_button.pack(pady=10)

    def open_settings(self):
        # Functionality to open settings screen
        settings_window = tk.Toplevel(self.root)
        SettingsScreen(settings_window)

    def one_time_connection(self):
        # One-Time Connection functionality
        print("One-Time Connection")
        # Implement one-time connection logic here

    def open_learn_more(self):
        # Open the ui_kb.py script
        subprocess.Popen(["python", "ui_kb.py"])

    def log_out(self):
        # Log out functionality
        print("Logging out...")
        # Implement log out logic here, such as closing this window and opening the login window
        self.root.destroy()  # Close the current window
        subprocess.Popen(["python", "ui_login.py"])  # Open the login window

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
        dark_mode_check.pack(pady=5)
        
        notifications_var = tk.BooleanVar(value=True)
        notifications_check = ttk.Checkbutton(general_settings_frame, text="Enable Notifications", variable=notifications_var, style="TCheckbutton")
        notifications_check.pack(pady=5)

        # Save Button
        save_button = ttk.Button(root, text="Save Settings", command=self.save_settings)
        save_button.pack(pady=20)

    def save_settings(self):
        # Save settings functionality
        print(f"App Status: {'On' if self.app_status.get() else 'Off'}")
        # Implement save logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamWatchApp(root)
    root.mainloop()
