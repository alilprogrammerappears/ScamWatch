import tkinter as tk
from tkinter import ttk
import webbrowser

class KnowledgeBasePage:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch Knowledge Base")
        self.root.geometry("600x600")

        # Set theme
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
        self.style.configure("TLabel", background="#FFFFFF", foreground="#4CAF50", font=("Helvetica", 12))
        self.style.configure("TEntry", font=("Helvetica", 12))

        # Background
        self.root.configure(bg="#2C3E50")

        # Title
        title = tk.Label(root, text="Knowledge Base", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
        title.pack(pady=10)

        # Search Bar
        search_frame = tk.Frame(root, bg="#2C3E50")
        search_frame.pack(pady=10)
        
        search_label = ttk.Label(search_frame, text="Search:", background="#2C3E50", foreground="#4CAF50")
        search_label.pack(side="left", padx=5)
        
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=5)
        
        search_button = ttk.Button(search_frame, text="Search", command=self.search)
        search_button.pack(side="left", padx=5)

        # Knowledge Base Content
        self.content_frame = tk.Frame(root, bg="#2C3E50")
        self.content_frame.pack(pady=10, fill="both", expand=True)
        
        self.content_text = tk.Text(self.content_frame, height=10, width=70, wrap="word", bg="white", fg="black", font=("Helvetica", 12))
        self.content_text.pack(pady=10, padx=10, fill="both", expand=True)

        # Links Section
        links_frame = tk.Frame(root, bg="#2C3E50")
        links_frame.pack(pady=10, fill="both", expand=True)

        links_label = ttk.Label(links_frame, text="Useful Links:", background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 14, "bold"))
        links_label.pack(anchor="w", padx=10)

        # Adding buttons for each link
        self.add_link_button(links_frame, "Five best practices to avoid falling prey to remote scammers", "https://example.com/best-practices")
        self.add_link_button(links_frame, "Anydesk - Abuse prevention", "https://example.com/anydesk-abuse-prevention")
        self.add_link_button(links_frame, "Remote access scams - All you need to know", "https://example.com/remote-access-scams")
        self.add_link_button(links_frame, "ConnectWise - How to avoid remote support scams", "https://example.com/connectwise-avoid-scams")
        self.add_link_button(links_frame, "Beware of Remote access scam alerts/notifications", "https://example.com/remote-access-alerts")
        self.add_link_button(links_frame, "Types of Remote access phishing scams", "https://example.com/types-of-phishing-scams")

        # Populate initial content
        self.display_content("Welcome to the ScamWatch Knowledge Base. Use the link above to find information about various types of scams.")

    def search(self):
        query = self.search_entry.get()
       
