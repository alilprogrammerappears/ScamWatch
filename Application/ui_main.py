import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw
from ui_settings import SettingsScreen
import logging
import subprocess
import os
import dbconnect

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

logging.getLogger('PIL').setLevel(logging.WARNING)

class ScamWatchApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("ScamWatch")
        self.root.geometry("800x700")

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#2C3E50", foreground="#FFFFFF", font=("Helvetica", 12))
        self.style.configure("TFrame", background="#2C3E50")
        
        # Background
        self.root.configure(bg="#2C3E50")

        # Configure grid to center elements
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Load and display image
        self.logo_image = Image.open("login_bg.png")
        self.logo_image = self.logo_image.resize((200, 200), Image.LANCZOS)

        # Create a circular mask
        mask = Image.new("L", self.logo_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + self.logo_image.size, fill=255)
        self.logo_image.putalpha(mask)

        # Apply mask to make image circular
        self.logo_image = ImageOps.fit(self.logo_image, mask.size, centering=(0.5, 0.5))
        self.logo_image.putalpha(mask)

        self.logo_photo = ImageTk.PhotoImage(self.logo_image, master=root)
        logo_label = tk.Label(root, image=self.logo_photo, bg="#2C3E50")
        logo_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons
        button_frame = tk.Frame(root, bg="#2C3E50")
        button_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="n")
        
        # Display the logged-in username
        username_button = ttk.Button(button_frame, text=f"User Name: {username}", command=self.show_profile)
        username_button.pack(pady=5)
        
        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(pady=5)

        learn_more_button = ttk.Button(button_frame, text="Learn More", command=self.open_learn_more)
        learn_more_button.pack(pady=5)

        logout_button = ttk.Button(button_frame, text="Log Out", command=self.log_out)
        logout_button.pack(pady=5)

        self.username = username  # Store the username for later use

    def show_profile(self):
        # Functionality to show user profile
        profile_window = tk.Toplevel(self.root)
        profile_window.title("User Profile")
        profile_window.geometry("400x300")
        profile_window.configure(bg="#2C3E50")
        
        profile_title = tk.Label(profile_window, text="User Profile", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#4CAF50")
        profile_title.pack(pady=10)
        
        # Fetch user data from the database
        user_info = dbconnect.get_user_info(self.username)

        username_label = tk.Label(profile_window, text=f"Username: {self.username}", font=("Helvetica", 14), bg="#2C3E50", fg="#FFFFFF")
        username_label.pack(pady=5)
        
        name_label = tk.Label(profile_window, text=f"Name: {user_info['name']}", font=("Helvetica", 14), bg="#2C3E50", fg="#FFFFFF")
        name_label.pack(pady=5)
        
        email_label = tk.Label(profile_window, text=f"Email: {user_info['email']}", font=("Helvetica", 14), bg="#2C3E50", fg="#FFFFFF")
        email_label.pack(pady=5)
        
        close_button = ttk.Button(profile_window, text="Close", command=profile_window.destroy)
        close_button.pack(pady=10)

    def open_settings(self):
        # Functionality to open settings screen
        settings_window = tk.Toplevel(self.root)
        current_user_id = 1
        app = SettingsScreen(settings_window, current_user_id=current_user_id)

    def open_learn_more(self):
        # Open the ui_kb.py script
        script_path = os.path.join(os.path.dirname(__file__), 'ui_kb.py')
        subprocess.Popen(["python", script_path])

    def log_out(self):
        # Log out functionality
        logging.info("Logging out...")
        self.root.destroy()  # Close the current window
        script_path = os.path.join(os.path.dirname(__file__), 'ui_login.py')
        subprocess.Popen(["python", script_path])  # Open the login window
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamWatchApp(root, "User")
    root.mainloop()
