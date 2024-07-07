import tkinter as tk
from tkinter import ttk
import webbrowser

class KnowledgeBase:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Knowledge Base")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        # Title
        title = tk.Label(root, text="Knowledge Base", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title.pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(root, bg="#f0f0f0")
        search_frame.pack(pady=10, fill="x")

        search_label = tk.Label(search_frame, text="Search:", bg="#f0f0f0", fg="#2c3e50")
        search_label.pack(side="left", padx=10)

        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=10)

        search_button = tk.Button(search_frame, text="Search", command=self.search)
        search_button.pack(side="left", padx=10)

        # Content Display Area
        self.content_text = tk.Text(root, wrap="word", height=20, width=80, bg="white", fg="black", font=("Helvetica", 12))
        self.content_text.pack(padx=10, pady=10)

        # Links Section
        links_frame = tk.Frame(root, bg="#2C3E50")
        links_frame.pack(pady=10)

        links_label = tk.Label(links_frame, text="Useful Links:", font=("Helvetica", 14, "bold"), bg="#2C3E50", fg="#4CAF50")
        links_label.pack(anchor="w", padx=10)

        links = [
            ("Five best practices to avoid falling prey to remote scammers", "https://www.goto.com/blog/five-best-practices-to-avoid-falling-prey-to-remote-scammers"),
            ("Anydesk - Abuse prevention", "https://anydesk.com/en/abuse-prevention"),
            ("Remote access scams - All you need to know", "https://goabacus.com/remote-access-scams-everything-you-need-to-know-to-avoid-falling-for-one/"),
            ("ConnectWise - How to avoid remote support scams", "https://www.connectwise.com/blog/rmm/how-to-avoid-remote-support-scams"),
            ("Beware of Remote access scam alerts/notifications", "https://wesaveyou.com/remote-access-scam-alert-did-someone-ask-you-to-download-software-to-access-your-electronic-device-dont-fall-for-it/"),
            ("Types of Remote access phishing scams", "https://www.fullview.io/blog/how-to-avoid-remote-access-scams")
        ]

        for text, url in links:
            link_button = tk.Button(links_frame, text=text, command=lambda url=url: self.open_link(url), bg="#4CAF50", fg="white")
            link_button.pack(fill="x", padx=10, pady=5)

    def search(self):
        # Placeholder for search functionality
        query = self.search_entry.get()
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(tk.END, f"Search results for: {query}")

    def open_link(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeBase(root)
    root.mainloop()
