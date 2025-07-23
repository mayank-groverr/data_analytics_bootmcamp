import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

BOOKS = {
    1: "1984",
    2: "To Kill a Mockingbird",
    3: "The Great Gatsby",
    4: "Pride and Prejudice",
    5: "The Catcher in the Rye",
    6: "Moby-Dick",
    7: "Jane Eyre",
    8: "Brave New World",
    9: "The Hobbit",
    10: "Fahrenheit 451",
    11: "Wuthering Heights",
    12: "Animal Farm",
    13: "Crime and Punishment",
    14: "The Odyssey",
    15: "The Brothers Karamazov",
    16: "War and Peace",
    17: "Frankenstein",
    18: "Dracula",
    19: "Great Expectations",
    20: "Les Misérables",
    21: "Don Quixote",
    22: "The Divine Comedy",
    23: "Ulysses",
    24: "The Iliad",
    25: "A Tale of Two Cities"
}

def init_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE NOT NULL,
            is_available INTEGER DEFAULT 1
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (book_id) REFERENCES books (id),
            UNIQUE(user_id, book_id)
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM books')
    if cursor.fetchone()[0] == 0:
        for book_id, title in BOOKS.items():
            cursor.execute('INSERT INTO books (id, title, is_available) VALUES (?, ?, 1)', (book_id, title))

    conn.commit()
    conn.close()

def get_user():
    username = input("Enter your username: ")

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        print(f"Welcome back, {username}!")
        user_id = user[0]
        cursor.execute('''
            SELECT b.id, b.title
            FROM borrowed_books bb
            JOIN books b ON bb.book_id = b.id
            WHERE bb.user_id = ?
        ''', (user_id,))
        borrowed = cursor.fetchall()

        if borrowed:
            print("Your borrowed books:")
            for book_id, title in borrowed:
                print(f"ID: {book_id} - {title}")
        else:
            print("No books borrowed yet.")
    else:
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        user_id = cursor.lastrowid
        conn.commit()
        print(f"New user {username} registered!")

    conn.close()
    return user_id

def borrow_book(user_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT b.id, b.title
        FROM books b
        WHERE b.id NOT IN (
            SELECT bb.book_id
            FROM borrowed_books bb
            WHERE bb.user_id = ?
        )
    ''', (user_id,))
    available_books = cursor.fetchall()

    if not available_books:
        print("No books available to borrow or you have already borrowed all books.")
        conn.close()
        return

    print("\nAvailable books:")
    for book_id, title in available_books:
        print(f"ID: {book_id} - {title}")

    try:
        book_id = int(input("\nEnter the book ID to borrow: "))
    except ValueError:
        print("Invalid book ID!")
        conn.close()
        return

    cursor.execute('''
        SELECT b.title
        FROM books b
        WHERE b.id = ? AND b.id NOT IN (
            SELECT bb.book_id
            FROM borrowed_books bb
            WHERE bb.user_id = ?
        )
    ''', (book_id, user_id))
    book = cursor.fetchone()

    if not book:
        print("Book not found or already borrowed by you!")
        conn.close()
        return

    cursor.execute('''
        INSERT INTO borrowed_books (user_id, book_id)
        VALUES (?, ?)
    ''', (user_id, book_id))

    conn.commit()
    conn.close()

    print(f"Successfully borrowed: {book[0]}")

def view_borrowed_books(user_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT b.id, b.title
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        WHERE bb.user_id = ?
    ''', (user_id,))
    borrowed = cursor.fetchall()
    conn.close()

    if not borrowed:
        print("No books borrowed.")
        return

    print("\nYour Borrowed Books:")
    for book_id, title in borrowed:
        print(f"ID: {book_id} - {title}")
    print(f"\nTotal Books Borrowed: {len(borrowed)}")

def return_book(user_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT b.id, b.title
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        WHERE bb.user_id = ?
    ''', (user_id,))
    borrowed_books = cursor.fetchall()

    if not borrowed_books:
        print("You haven't borrowed any books.")
        conn.close()
        return

    print("Your borrowed books:")
    for book_id, title in borrowed_books:
        print(f"ID: {book_id} - {title}")

    try:
        book_id = int(input("\nEnter the book ID to return: "))
    except ValueError:
        print("Invalid book ID!")
        conn.close()
        return

    cursor.execute('''
        SELECT b.title
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        WHERE bb.user_id = ? AND bb.book_id = ?
    ''', (user_id, book_id))
    result = cursor.fetchone()

    if not result:
        print("You haven't borrowed this book.")
        conn.close()
        return

    cursor.execute('''
        DELETE FROM borrowed_books
        WHERE user_id = ? AND book_id = ?
    ''', (user_id, book_id))
    conn.commit()
    conn.close()
    print(f"Successfully returned: {result[0]}")


def main():
    init_database()
    user_id = get_user()
    while True:
        print("\n1. Borrow Book")
        print("2. View Borrowed Books")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            borrow_book(user_id)
        elif choice == '2'  :
            view_borrowed_books(user_id)
        elif choice == '3':
            return_book(user_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")



main()
