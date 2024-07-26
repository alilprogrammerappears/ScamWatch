import mysql.connector
from mysql.connector import Error

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
        print(f"Error: {e}")
        return None

def authenticate_user(username, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        connection.close()
        return result
    else:
        print("Failed to connect to the database")
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
            print(f"Failed to sign up: {e}")
            return False
        finally:
            connection.close()
    else:
        print("Failed to connect to the database")
        return False

# get_trusted_email
# returns email which is sent to process_blocking for sending an alert
