import mysql.connector
from mysql.connector import Error

# Database connection details
DB_HOST = "swatch.cvuie4ieiptg.us-east-2.rds.amazonaws.com"
DB_PORT = 3306
DB_USER = "admin"
DB_PASSWORD = "scamwatch"
DB_NAME = "scamwatch_users"  # Use the correct database name

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
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
    return None

def register_user(name, username, password, email):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, username, password, email))
            connection.commit()
            connection.close()
            return True
        except Error as e:
            print(f"Failed to sign up: {e}")
            connection.close()
    return False

