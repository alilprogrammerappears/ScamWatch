import smtplib
import json
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert_email(trusted_contact_email):

    try:

        file_path="config.json"
        with open(file_path, "r") as file:
            config = json.load(file)
            scamwatch_email = config.get("scamwatch_email")
            scamwatch_password = config.get("scamwatch_password")
            email_subject = config.get("subject")
            email_message = config.get("message_body")
    except FileNotFoundError:
        logging.info("Configuration file not found.")
    except json.JSONDecodeError:
        logging.error("Error decoding configuration file.")

    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = scamwatch_email
        msg['To'] = trusted_contact_email
        msg['Subject'] = email_subject
        
        # Attach the email body
        msg.attach(MIMEText(email_message, 'plain'))
        
        # Set up the server connection
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(scamwatch_email, scamwatch_password)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(scamwatch_email, trusted_contact_email, text)
        
        # Disconnect from the server
        server.quit()
        
        logging.info(f"Alert email sent to {trusted_contact_email}.")
    except Exception as e:
        logging.error(f"Failed to send email. Error: {e}")


