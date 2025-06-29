import sqlite3

class SQLite_helper:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.user_table()

    def user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            acc_balance REAL DEFAULT 0.00
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
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self.execute_query(query, (username, password))

    def login_user(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        return self.fetch_all()
    
    def update_password(self, username, new_password):
        query = "UPDATE users SET password = ? WHERE username = ?"
        self.execute_query(query, (new_password, username))

    def update_username(self, old_username, password, new_username):
        query = "UPDATE users SET username = ? WHERE username = ? AND password = ?"
        self.execute_query(query, (new_username, old_username, password))

    def delete_user(self, username):
        query = "DELETE FROM users WHERE username = ?"
        self.execute_query(query, (username,))

    def deposit(self, username, password, amount):  
        query = "UPDATE users SET acc_balance = acc_balance + ? WHERE username = ? AND password = ?"
        self.execute_query(query, (amount, username, password))

    def withdraw(self, username, password, amount):
        query = "UPDATE users SET acc_balance = acc_balance - ? WHERE username = ? AND password = ?"
        self.execute_query(query, (amount, username, password))

    def get_balance(self, username, password):
        query = "SELECT acc_balance FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        result = self.fetch_all()
        return result[0][0] if result else None

    def fetch_all(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()