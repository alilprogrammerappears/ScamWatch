import mysql.connector
from mysql.connector import Error
import logging

# Set up log file
log_file = 'ScamWatch.log'

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='swatch.cvuie4ieiptg.us-east-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            password='scamwatch',
            database='scamwatch_users'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        logging.error(f"Error: {e}")
        return None

def authenticate_user(username, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        connection.close()
        return result
    else:
        logging.error("Failed to connect to the database")
        return None

def register_user(name, username, password, email):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, username, password, email))
            connection.commit()
            return True
        except Error as e:
            logging.error(f"Failed to sign up: {e}")
            return False
        finally:
            connection.close()
    else:
        logging.error("Failed to connect to the database")
        return False

def get_user_info(username):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT name, email FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user_info = cursor.fetchone()
        connection.close()
        return user_info
    else:
        logging.error("Failed to connect to the database")
        return None

def get_trusted_emails(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT email FROM trustedusers WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        emails = [row['email'] for row in cursor.fetchall()]
        connection.close()
        return emails
    else:
        logging.error("Failed to connect to the database")
        return []
