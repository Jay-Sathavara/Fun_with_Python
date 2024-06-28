
import sqlite3
from tkinter import *
from tkinter import messagebox
import hashlib

def setup_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL)''')
    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    conn.close()


def check_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user



setup_db()

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("400x400")
        self.current_user = None

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()
        
        Label(self.root, text="Username").pack(pady=10)
        self.username_entry = Entry(self.root)
        self.username_entry.pack(pady=5)
        
        Label(self.root, text="Password").pack(pady=10)
        self.password_entry = Entry(self.root, show='*')
        self.password_entry.pack(pady=5)
        
        Button(self.root, text="Login", command=self.login).pack(pady=20)
        Button(self.root, text="Register", command=self.register).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_user(username, password):
            self.current_user = username
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        add_user(username, password)
        messagebox.showinfo("Success", "User registered successfully")

