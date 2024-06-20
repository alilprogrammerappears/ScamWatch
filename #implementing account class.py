#implementing account class

import mysql.connector
from mysql.connector import Error

class Account:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

    def change_username(self, user_id, new_username):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE accounts SET username = %s WHERE id = %s"
                cursor.execute(query, (new_username, user_id))
                connection.commit()
                cursor.close()
                connection.close()
                print("Username updated successfully.")
        except Error as e:
            print(f"Error updating username: {e}")

    def change_password(self, user_id, new_password):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE accounts SET password = %s WHERE id = %s"
                cursor.execute(query, (new_password, user_id))
                connection.commit()
                cursor.close()
                connection.close()
                print("Password updated successfully.")
        except Error as e:
            print(f"Error updating password: {e}")

    def change_email(self, user_id, new_email):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE accounts SET email = %s WHERE id = %s"
                cursor.execute(query, (new_email, user_id))
                connection.commit()
                cursor.close()
                connection.close()
                print("Email updated successfully.")
        except Error as e:
            print(f"Error updating email: {e}")

# Usage example
if __name__ == "__main__":
    db_config = {
        'host': 'scamwatch.c9eg4kuesca7.us-east-2.rds.amazonaws.com',
        'port': 3306,
        'user': 'SWadmin',
        'password': 'scamwatch',
        'database': 'scamwatch_users'
    }

    account = Account(db_config)

    # Change username example
    account.change_username(1, 'SWadmin')

    # Change password example
    account.change_password(1, 'scamwatch')

    # Change email example
    account.change_email(1, 'anmolmazoo@yahoo.com')
