import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert_email(user_email, user_password, to_email, subject, message):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = user_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(message, 'plain'))
        
        # Set up the server connection
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(user_email, user_password)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(user_email, to_email, text)
        
        # Disconnect from the server
        server.quit()
        
        print(f"Alert email sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
user_email = 'scamwatchalerts@outlook.com'
user_password = 'hhddjsmxdreqpkpi'
# Fetch and add the emergency contact email below:
to_email = 'arshdeep.singh27@student.kpu.ca' 
subject = 'ScamWatch Alert: Remote Access Attempt Detected'
message = '''
Dear User,

We would like to inform you that a remote access attempt has been detected on [Relative's Name]’s system. Please take immediate action to secure the system.

Thank you for your prompt attention to this matter.

Regards,
ScamWatch
'''

send_alert_email(user_email, user_password, to_email, subject, message)
