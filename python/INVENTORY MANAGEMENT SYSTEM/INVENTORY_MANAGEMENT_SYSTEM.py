
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

    def create_main_screen(self):
        self.clear_screen()
        
        Label(self.root, text="Welcome, " + self.current_user).pack(pady=10)
        
        Button(self.root, text="Add Product", command=self.add_product_screen).pack(pady=5)
        Button(self.root, text="View Products", command=self.view_products).pack(pady=5)
        Button(self.root, text="Generate Reports", command=self.generate_reports_screen).pack(pady=5)
        Button(self.root, text="Low-Stock Alerts", command=self.low_stock_alerts).pack(pady=5)
        Button(self.root, text="Logout", command=self.create_login_screen).pack(pady=20)

    def add_product_screen(self):
        self.clear_screen()
        
        Label(self.root, text="Product Name").pack(pady=10)
        self.product_name_entry = Entry(self.root)
        self.product_name_entry.pack(pady=5)
        
        Label(self.root, text="Quantity").pack(pady=10)
        self.product_quantity_entry = Entry(self.root)
        self.product_quantity_entry.pack(pady=5)
        
        Label(self.root, text="Price").pack(pady=10)
        self.product_price_entry = Entry(self.root)
        self.product_price_entry.pack(pady=5)
        
        Button(self.root, text="Add Product", command=self.add_product).pack(pady=20)
        Button(self.root, text="Back", command=self.create_main_screen).pack(pady=5)

    def add_product(self):
        name = self.product_name_entry.get()
        quantity = int(self.product_quantity_entry.get())
        price = float(self.product_price_entry.get())
        
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Product added successfully")
        self.create_main_screen()

    def view_products(self):
        self.clear_screen()

        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        conn.close()

        for product in products:
            Label(self.root, text=f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}").pack(pady=5)
            Button(self.root, text="Edit", command=lambda p=product: self.edit_product_screen(p)).pack(pady=5)
            Button(self.root, text="Delete", command=lambda p=product: self.delete_product(p[0])).pack(pady=5)

        Button(self.root, text="Back", command=self.create_main_screen).pack(pady=20)

    def edit_product_screen(self, product):
        self.clear_screen()

        Label(self.root, text="Edit Product").pack(pady=10)
        
        Label(self.root, text="Product Name").pack(pady=10)
        self.product_name_entry = Entry(self.root)
        self.product_name_entry.insert(0, product[1])
        self.product_name_entry.pack(pady=5)
        
        Label(self.root, text="Quantity").pack(pady=10)
        self.product_quantity_entry = Entry(self.root)
        self.product_quantity_entry.insert(0, product[2])
        self.product_quantity_entry.pack(pady=5)
        
        Label(self.root, text="Price").pack(pady=10)
        self.product_price_entry = Entry(self.root)
        self.product_price_entry.insert(0, product[3])
        self.product_price_entry.pack(pady=5)
        
        Button(self.root, text="Save Changes", command=lambda: self.edit_product(product[0])).pack(pady=20)
        Button(self.root, text="Back", command=self.view_products).pack(pady=5)

    def edit_product(self, product_id):
        name = self.product_name_entry.get()
        quantity = int(self.product_quantity_entry.get())
        price = float(self.product_price_entry.get())

        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, product_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product updated successfully")
        self.view_products()

    def delete_product(self, product_id):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product deleted successfully")
        self.view_products()

    def generate_reports_screen(self):
        self.clear_screen()
        
        Label(self.root, text="Sales Summary").pack(pady=10)
        
        Button(self.root, text="Back", command=self.create_main_screen).pack(pady=20)

    def low_stock_alerts(self):
        self.clear_screen()
        
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE quantity < 5') 
        products = cursor.fetchall()
        conn.close()

        Label(self.root, text="Low-Stock Products").pack(pady=10)
        for product in products:
            Label(self.root, text=f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}").pack(pady=5)
        
        Button(self.root, text="Back", command=self.create_main_screen).pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    app = InventoryApp(root)
    root.mainloop()