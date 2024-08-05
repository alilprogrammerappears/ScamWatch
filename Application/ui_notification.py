import tkinter as tk
from tkinter import ttk
import webbrowser
import queue
import threading
import logging

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Create a queue to communicate between threads
alert_queue = queue.Queue()

def open_link(url):
    webbrowser.open(url)

def show_custom_alert():

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    def process_queue():
        try:
            # Check the queue for new messages
            message = alert_queue.get_nowait()
            if message == "show_alert":
                alert_window = tk.Toplevel(root)
                alert_window.title("ScamWatch Alert")
                alert_window.geometry("450x250")
                alert_window.configure(bg="#2C3E50")

                message = ("We've just blocked a remote connection attempt to your system. This could be a potential scam. "
                            "\n\nPlease review these resources to learn more about staying safe online by clicking the button below. "
                            "\n\nIf you have a trusted contact set up, they have been notified about this incident.")
    
                message_label = ttk.Label(alert_window, text=message, wraplength=350, background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
                message_label.pack(pady=20, padx=20)
                
                # Frame for buttons
                button_frame = tk.Frame(alert_window, bg="#2C3E50")
                button_frame.pack(pady=10)

                kb_button = ttk.Button(button_frame, text="Open Knowledge Base", command=lambda: open_knowledge_base(alert_window), style="TButton")
                kb_button.pack(side="left", padx=10)

                # Center the alert window
                alert_window.update_idletasks()
                width = alert_window.winfo_width()
                height = alert_window.winfo_height()
                x = (alert_window.winfo_screenwidth() // 2) - (width // 2)
                y = (alert_window.winfo_screenheight() // 2) - (height // 2)
                alert_window.geometry(f'{width}x{height}+{x}+{y}')
    
        except queue.Empty:
            pass

        root.after(100, process_queue)

    # Start the queue processing
    root.after(100, process_queue)
    root.mainloop()

def open_knowledge_base(parent_window):
    kb_window = tk.Toplevel(parent_window)
    kb_window.title("Knowledge Base")
    kb_window.geometry("600x400")
    kb_window.configure(bg="#2C3E50")

    kb_title = tk.Label(kb_window, text="Knowledge Base", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#4CAF50")
    kb_title.pack(pady=10)

    kb_message = ("Learn more about avoiding scams and keeping your system secure. "
                  "Here are some helpful resources:")
    
    kb_label = ttk.Label(kb_window, text=kb_message, wraplength=550, background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
    kb_label.pack(pady=20, padx=20)

    # Define the links
    links = [
        ("Anydesk - Abuse prevention", "https://anydesk.com/en/abuse-prevention"),
        ("Remote access scams - All you need to know", "https://goabacus.com/remote-access-scams-everything-you-need-to-know-to-avoid-falling-for-one/"),
        ("ConnectWise - How to avoid remote support scams", "https://www.connectwise.com/blog/rmm/how-to-avoid-remote-support-scams"),
        ("Beware of Remote access scam alerts/notifications", "https://wesaveyou.com/remote-access-scam-alert-did-someone-ask-you-to-download-software-to-access-your-electronic-device-dont-fall-for-it/"),
        ("Types of Remote access phishing scams", "https://www.fullview.io/blog/how-to-avoid-remote-access-scams")
    ]

    for text, url in links:
        link_button = ttk.Button(kb_window, text=text, command=lambda url=url: open_link(url), style="TButton")
        link_button.pack(fill="x", padx=20, pady=5)

    close_button = ttk.Button(kb_window, text="Close", command=kb_window.destroy, style="TButton")
    close_button.pack(pady=10)


# Apply custom styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
style.configure("TLabel", background="#FFFFFF", foreground="#4CAF50", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))


# Start the Tkinter alert thread
alert_thread = threading.Thread(target=show_custom_alert)
alert_thread.daemon = True  # Ensure it exits when the main program exits
alert_thread.start()