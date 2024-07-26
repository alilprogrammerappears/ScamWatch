import tkinter as tk
from tkinter import ttk
import queue
import threading

# Create a queue to communicate between threads
alert_queue = queue.Queue()

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

                message_text = ("We've just blocked a remote connection attempt to your system. This could be a potential scam. "
                                "\n\nPlease review these resources to learn more about staying safe online: [Knowledgebase Page Link]. "
                                "\n\nIf you have a trusted contact set up, they have been notified about this incident.")

                message_label = ttk.Label(alert_window, text=message_text, wraplength=350, background="#2C3E50", foreground="#4CAF50", font=("Helvetica", 12))
                message_label.pack(pady=20, padx=20)

                ok_button = ttk.Button(alert_window, text="OK", command=alert_window.destroy, style="TButton")
                ok_button.pack(pady=10)

                # Center the alert window
                alert_window.update_idletasks()
                width = alert_window.winfo_width()
                height = alert_window.winfo_height()
                x = (alert_window.winfo_screenwidth() // 2) - (width // 2)
                y = (alert_window.winfo_screenheight() // 2) - (height // 2)
                alert_window.geometry(f'{width}x{height}+{x}+{y}')
        except queue.Empty:
            pass
        # Check the queue again after 100ms
        root.after(100, process_queue)

    # Start the queue processing
    root.after(100, process_queue)
    root.mainloop()

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
