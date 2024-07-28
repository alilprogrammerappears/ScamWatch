import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw
import subprocess
import dbconnect  # Import the dbconnect module

# This is the main ScamWatch window file

class ScamWatchApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("ScamWatch")
        self.root.geometry("800x700")  # Adjusted window size to fit all elements

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
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Title
        title = tk.Label(root, text="ScamWatch", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="n")

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

        # Placeholder for summaries
        placeholder_label = tk.Label(root, text="Placeholder for future content", bg="#2C3E50", fg="#4CAF50")
        placeholder_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="n")
        placeholder_text = tk.Text(root, height=10, width=50)
        placeholder_text.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

        # Buttons
        button_frame = tk.Frame(root, bg="#2C3E50")
        button_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="n")
        
        # Display the logged-in username
        username_button = ttk.Button(button_frame, text=f"User Name: {username}", command=self.show_profile)
        username_button.pack(pady=5)
        
        settings_button = ttk.Button(button_frame, text="Settings", command=self.open_settings)
        settings_button.pack(pady=5)

        learn_more_button = ttk.Button(button_frame, text="Learn More", command=self.open_learn_more)
        learn_more_button.pack(pady=5)

        logout_button = ttk.Button(button_frame, text="Log Out", command=self.log_out)
        logout_button.pack(pady=5)

    def show_profile(self):
        # Functionality to show user profile
        profile_window = tk.Toplevel(self.root)
        profile_window.title("User Profile")
        profile_window.geometry("400x300")
        profile_window.configure(bg="#2C3E50")
        
        profile_title = tk.Label(profile_window, text="User Profile", font=("Helvetica", 18, "bold"), bg="#2C3E50", fg="#4CAF50")
        profile_title.pack(pady=10)
        
        current_user = dbconnect.get_current_user()
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
        subprocess.Popen(["python", "ui_settings.py"])

    def open_learn_more(self):
        # Open the ui_kb.py script
        subprocess.Popen(["python", "ui_kb.py"])

    def log_out(self):
        # Log out functionality
        print("Logging out...")
        # Implement log out logic here, such as closing this window and opening the login window
        self.root.destroy()  # Close the current window
        subprocess.Popen(["python", "ui_login.py"])  # Open the login window

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamWatchApp(root, "User")
    root.mainloop()
