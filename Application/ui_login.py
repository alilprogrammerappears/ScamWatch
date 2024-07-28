import sys
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw
import dbconnect  # Import the dbconnect module

# Add the project's root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Application.ui_main import ScamWatchApp  # Import the main application class

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Login")
        self.root.geometry("400x450")
        
        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#FFFFFF", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))

        # Background
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="ScamWatch Login", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.pack(pady=10)

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
        logo_label.pack(pady=10)

        # Username
        username_label = ttk.Label(root, text="Username", background="#2C3E50", foreground="#4CAF50")
        username_label.pack(pady=5)
        self.username_entry = ttk.Entry(root, width=30)
        self.username_entry.pack(pady=5)

        # Password
        password_label = ttk.Label(root, text="Password", background="#2C3E50", foreground="#4CAF50")
        password_label.pack(pady=5)
        self.password_entry = ttk.Entry(root, width=30, show="*")
        self.password_entry.pack(pady=5)

        # Error message label
        self.error_message = tk.Label(root, text="", font=("Helvetica", 10), bg="#2C3E50", fg="red")
        self.error_message.pack(pady=5)

        # Login Button
        login_button = ttk.Button(root, text="Login", command=self.login)
        login_button.pack(pady=20)

        # Sign Up Button
        signup_button = ttk.Button(root, text="Sign Up", command=self.open_signup_window)
        signup_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        result = dbconnect.authenticate_user(username, password)
        if result:
            print("Login successful")
            self.root.destroy()  # Close the login window
            root = tk.Tk()  # Create a new root window
            app = ScamWatchApp(root, username)  # Open the main application window
            root.mainloop()
        else:
            self.error_message.config(text="Try again with correct Username/password")

    def open_signup_window(self):
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.title("Sign Up")
        self.signup_window.geometry("400x450")
        
        # Name
        name_label = ttk.Label(self.signup_window, text="Name")
        name_label.pack(pady=5)
        self.name_entry = ttk.Entry(self.signup_window, width=30)
        self.name_entry.pack(pady=5)
        
        # Username
        username_label = ttk.Label(self.signup_window, text="Username")
        username_label.pack(pady=5)
        self.signup_username_entry = ttk.Entry(self.signup_window, width=30)
        self.signup_username_entry.pack(pady=5)

        # Password
        password_label = ttk.Label(self.signup_window, text="Password")
        password_label.pack(pady=5)
        self.signup_password_entry = ttk.Entry(self.signup_window, width=30, show="*")
        self.signup_password_entry.pack(pady=5)

        # Email
        email_label = ttk.Label(self.signup_window, text="Email")
        email_label.pack(pady=5)
        self.email_entry = ttk.Entry(self.signup_window, width=30)
        self.email_entry.pack(pady=5)

        # Sign Up Button
        signup_button = ttk.Button(self.signup_window, text="Sign Up", command=self.signup)
        signup_button.pack(pady=20)

    def signup(self):
        name = self.name_entry.get()
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        email = self.email_entry.get()
        
        success = dbconnect.register_user(name, username, password, email)
        if success:
            print("Sign up successful")
            self.signup_window.destroy()  # Close the signup window
        else:
            print("Failed to sign up")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
