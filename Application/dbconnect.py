import mysql.connector

# Database connection details
DB_HOST = "swatch.cvuie4ieiptg.us-east-2.rds.amazonaws.com"
DB_PORT = 3306
DB_USER = "admin"
DB_PASSWORD = "scamwatch"
DB_NAME = "swatch"

def get_current_user():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE user_id = 1")  # Change this query as per your schema
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        else:
            return "Unknown User"
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Unknown User"
