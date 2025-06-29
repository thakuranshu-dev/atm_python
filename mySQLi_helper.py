import mysql.connector

class MySQLI_helper:
    def __init__(self, host, port, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            acc_balance DECIMAL(10, 2) DEFAULT 0.00,
        )
        """
        self.execute_query(query)

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()

    def register_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.execute_query(query, (username, password))

    def login_user(self, username, password):
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.execute_query(query, (username, password))
        return self.fetch_all()
    
    def update_password(self, username, new_password):
        query = "UPDATE users SET password = %s WHERE username = %s"
        self.execute_query(query, (new_password, username))

    def deposit(self, username, amount):  
        query = "UPDATE users SET acc_balance = acc_balance + %s WHERE username = %s"
        self.execute_query(query, (amount, username))

    def withdraw(self, username, amount):
        query = "UPDATE users SET acc_balance = acc_balance - %s WHERE username = %s"
        self.execute_query(query, (amount, username))

    def get_balance(self, username):
        query = "SELECT acc_balance FROM users WHERE username = %s"
        self.execute_query(query, (username,))
        result = self.fetch_all()
        return result[0][0] if result else None

    def fetch_all(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()