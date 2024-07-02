import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

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

        # Login Button
        login_button = ttk.Button(root, text="Login", command=self.login)
        login_button.pack(pady=20)

        # Sign Up Button
        signup_button = ttk.Button(root, text="Sign Up", command=self.signup)
        signup_button.pack()

    def login(self):
        # Login functionality
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Logging in with Username: {username} and Password: {password}")
        # Implement actual login logic here

    def signup(self):
        # Sign Up functionality
        print("Navigating to Sign Up screen")
        # Implement navigation to sign up screen here

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()
