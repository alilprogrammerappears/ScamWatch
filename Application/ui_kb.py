import tkinter as tk
from tkinter import ttk
import webbrowser
import logging
from PIL import Image, ImageTk, ImageOps, ImageDraw

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

logging.getLogger('PIL').setLevel(logging.WARNING)


class KnowledgeBase:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Knowledge Base")
        self.root.geometry("600x600")
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="Knowledge Base", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.pack(pady=10)

        # Load and display image
        self.logo_image = Image.open("login_bg.png")
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

        # Links Section
        links_frame = tk.Frame(root, bg="#2C3E50")
        links_frame.pack(pady=10)

        links_label = tk.Label(links_frame, text="Useful Links:", font=("Helvetica", 14, "bold"), bg="#2C3E50", fg="#4CAF50")
        links_label.pack(anchor="w", padx=10)

        links = [
            ("Anydesk - Abuse prevention", "https://anydesk.com/en/abuse-prevention"),
            ("Remote access scams - All you need to know", "https://goabacus.com/remote-access-scams-everything-you-need-to-know-to-avoid-falling-for-one/"),
            ("ConnectWise - How to avoid remote support scams", "https://www.connectwise.com/blog/rmm/how-to-avoid-remote-support-scams"),
            ("Beware of Remote access scam alerts/notifications", "https://wesaveyou.com/remote-access-scam-alert-did-someone-ask-you-to-download-software-to-access-your-electronic-device-dont-fall-for-it/"),
            ("Types of Remote access phishing scams", "https://www.fullview.io/blog/how-to-avoid-remote-access-scams")
        ]

        for text, url in links:
            link_button = tk.Button(links_frame, text=text, command=lambda url=url: self.open_link(url), bg="#4CAF50", fg="#FFFFFF")
            link_button.pack(fill="x", padx=10, pady=5)


    def open_link(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeBase(root)
    root.mainloop()
