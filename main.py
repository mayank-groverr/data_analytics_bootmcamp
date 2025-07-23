import sqlite3

ITEMS = {
    "apple": 1.50,
    "banana": 0.80,
    "milk": 3.20,
    "bread": 2.50,
    "eggs": 4.00,
    "rice": 5.75
}

def init_database():
    conn = sqlite3.connect("grocery_store.db")
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS orders')
    cursor.execute('DROP TABLE IF EXISTS customers')

    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
    ''')

    conn.commit()
    conn.close()

def get_customer():
    username = input("Enter username: ")

    conn = sqlite3.connect("grocery_store.db")
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM customers WHERE username = ?', (username,))
    customer = cursor.fetchone()

    if customer:
        print(f"Welcome back {username}!")
        customer_id = customer[0]
        cursor.execute('''
            SELECT item_name, quantity, price
            FROM orders
            WHERE customer_id = ?
        ''', (customer_id,))
        orders = cursor.fetchall()

        if orders:
            print("Your existing orders:")
            total = 0
            for order in orders:
                order_total = order[1] * order[2]
                total += order_total
                print(f"Item: {order[0]}, Quantity: {order[1]}, Price: ${order[2]:.2f}, Total: ${order_total:.2f}")
            print(f"Total spent: ${total:.2f}")
        else:
            print("No previous orders found.")
    else:
        cursor.execute('INSERT INTO customers (username) VALUES (?)', (username,))
        customer_id = cursor.lastrowid
        conn.commit()
        print(f"New customer {username} created!")

    conn.close()
    return customer_id

def add_order(customer_id):
    print("\nAvailable items:")
    for item, price in ITEMS.items():
        print(f"{item}: ${price:.2f}")

    item_name = input("\nEnter item name: ")
    if item_name not in ITEMS:
        print("Item not available!")
        return

    quantity = int(input("Enter quantity: "))
    price = ITEMS[item_name]

    conn = sqlite3.connect("grocery_store.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (customer_id, item_name, quantity, price)
        VALUES (?, ?, ?, ?)
    ''', (customer_id, item_name, quantity, price))
    conn.commit()
    conn.close()

    print(f"Order added: {quantity} x {item_name} at ${price:.2f} each")

def view_orders(customer_id):
    conn = sqlite3.connect("grocery_store.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT item_name, quantity, price
        FROM orders
        WHERE customer_id = ?
    ''', (customer_id,))
    orders = cursor.fetchall()
    conn.close()

    if not orders:
        print("No orders found!")
        return

    total_bill = 0
    for order in orders:
        total = order[1] * order[2]
        total_bill += total
        print(f"Item: {order[0]}, Quantity: {order[1]}, Price: ${order[2]:.2f}, Total: ${total:.2f}")
    print(f"\nTotal Bill: ${total_bill:.2f}")

def main():
    init_database()

    customer_id = get_customer()

    while True:
        print("\n1. Add Order")
        print("2. View Orders")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_order(customer_id)
        elif choice == '2':
            view_orders(customer_id)
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
