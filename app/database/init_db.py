from app.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

# Customers table

cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS customers(
                   customer_id TEXT PRIMARY KEY,
                   name TEXT,
                   email TEXT,
                   plan TEXT,
                   status TEXT
               )
               """
)

# Orders table
cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS orders(
                   order_id TEXT PRIMARY KEY,
                   customer_id TEXT,
                   amount REAL,
                   status TEXT,
                   FOREIGN KEY(customer_id)
                   REFERENCES customers(customer_id)
               )
               """
)

# Sample customers
cursor.executemany(
    "INSERT OR REPLACE INTO customers VALUES (?, ?, ?, ?, ?)",
    [
        ("1001", "Rahul", "rahul@gmail.com", "Premium", "Active"),
        ("1002", "Sneha", "sneha@gmail.com", "Basic", "Expired"),
    ],
)

# Sample orders
cursor.executemany(
    "INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?)",
    [
        ("5001", "1001", 999, "Delivered"),
        ("5002", "1002", 499, "Refund Initiated"),
    ],
)

conn.commit()
conn.close()

print("✅ Database initialized successfully.")
