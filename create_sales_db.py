import sqlite3

# Connect to SQLite database (this creates sales_data.db in your current folder)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Drop the table if it already exists (to reset for testing)
cursor.execute("DROP TABLE IF EXISTS sales")

# Create the sales table
cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        "Price(Rs.)" REAL
    )
""")

# Sample data
sales_data = [
    ('Apple', 10, 30),
    ('Banana', 20, 5),
    ('Orange', 15, 10),
    ('Grapes', 8, 60),
    ('Mango', 12, 50),
    ('Pineapple', 5, 80),
    ('Strawberry', 18, 120),
    ('Watermelon', 3, 90),
    ('Kiwi', 7, 35),
    ('Papaya', 6, 40),
    ('Cherry', 10, 150),
    ('Blueberry', 4, 200),
    ('Peach', 9, 70),
    ('Plum', 11, 45),
    ('Pear', 14, 55),
    ('Apple', 6, 30),
    ('Banana', 9, 5),
    ('Mango', 8, 50),
    ('Grapes', 13, 60),
    ('Pineapple', 4, 80),
    ('Orange', 10, 10),
    ('Kiwi', 5, 35),
    ('Watermelon', 2, 90),
    ('Cherry', 6, 150),
    ('Strawberry', 7, 120),
    ('Peach', 3, 70),
    ('Blueberry', 2, 200),
    ('Papaya', 8, 40)
]

# Insert data into the table
cursor.executemany('INSERT INTO sales (product, quantity, "Price(Rs.)") VALUES (?, ?, ?)', sales_data)

# Commit and close
conn.commit()
conn.close()

print("sales_data.db created with sample sales data.")
