#Scamwatch UI Design code

import tkinter as tk
from tkinter import ttk

class ScamWatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamWatch")

        # Title
        title = tk.Label(root, text="ScamWatch", font=("Helvetica", 24))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Username and Settings
        username_label = tk.Label(root, text="User Name")
        username_label.grid(row=0, column=3, sticky="e")
        settings_button = ttk.Button(root, text="Settings")
        settings_button.grid(row=0, column=4, sticky="e")

        # Statistics
        stats_frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
        stats_frame.grid(row=1, column=3, rowspan=2, columnspan=2, pady=10, sticky="nsew")
        stats_label = tk.Label(stats_frame, text="Statistics", bg="lightgray", font=("Helvetica", 16))
        stats_label.grid(row=0, column=0, columnspan=2, pady=5)
        
        detected_label = tk.Label(stats_frame, text="Number of Scams detected", bg="lightgray")
        detected_label.grid(row=1, column=0, sticky="w")
        detected_value = tk.Label(stats_frame, text="0", bg="white", width=10)
        detected_value.grid(row=1, column=1, sticky="e")
        
        prevented_label = tk.Label(stats_frame, text="Number of Scams prevented", bg="lightgray")
        prevented_label.grid(row=2, column=0, sticky="w")
        prevented_value = tk.Label(stats_frame, text="0", bg="white", width=10)
        prevented_value.grid(row=2, column=1, sticky="e")

        # Summary
        summary_label = tk.Label(root, text="Summary of recent scam alerts or notifications")
        summary_label.grid(row=2, column=0, columnspan=3, pady=5)
        summary_text = tk.Text(root, height=10, width=50)
        summary_text.grid(row=3, column=0, columnspan=3, pady=10)

        # Learn More Button
        learn_more_button = ttk.Button(root, text="Learn More")
        learn_more_button.grid(row=4, column=0, columnspan=5, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamWatchApp(root)
    root.mainloop()
