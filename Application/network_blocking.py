import psutil
import smtplib
import tkinter as tk  # or
import subprocess

#scapy - Capture network packets and analyze them to identify remote connection attempts
def capture_packets():
    packets = sniff(count=100)
    packets.summary()

#Psutil - Monitor system and network activity to detect suspicious behavior
def monitor_network():
    connections = psutil.net_connections()
    for conn in connections:
        print(conn)

#subprocess - to block connections based on the identified unauthorized attempts
def block_ip(ip_address):
    subprocess.call(['iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])

#Email Notification

def send_email_notification(to_email, subject, message):
    from_email = 'your_email@example.com'
    password = 'your_password'
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, password)
    email_message = f'Subject: {subject}\n\n{message}'
    server.sendmail(from_email, to_email, email_message)
    server.quit()

#sms notifictaion

def send_sms_notification(to_number, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_='+1234567890', to=to_number)

#desktop Notification

def desktop_notification(message):
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showinfo("Alert", message)
