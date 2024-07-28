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
        cursor = connection.cursor(dictionary=True)
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
        print("Failed to connect to the database")
        return None

def get_trusted_email():
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT email FROM trusted_users LIMIT 1"  # Modify query as needed
        cursor.execute(query)
        trusted_email = cursor.fetchone()
        connection.close()
        return trusted_email['email'] if trusted_email else None
    else:
        print("Failed to connect to the database")
        return None
