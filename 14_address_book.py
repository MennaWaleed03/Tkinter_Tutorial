# 16_address_book.py
# A simple Address Book application using Tkinter and SQLite
# Allows adding, viewing, and deleting contacts

from tkinter import Tk, Label, Entry, Button, END, W
import sqlite3

# -------------------------
# Step 1: Create main window and connect to database
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Address Book")

# Connect to SQLite database
# sqlite3.connect("file.db"): creates database file if it doesn't exist
conn = sqlite3.connect("address_book.db")
c = conn.cursor()

# Uncomment below to create table initially
# c.execute("""
# CREATE TABLE addresses(
#     first_name TEXT,
#     last_name TEXT,
#     address TEXT,
#     city TEXT,
#     state TEXT,
#     zipcode INTEGER
# )
# """)
# conn.commit()

# -------------------------
# Step 2: Define functions

def submit():
    """Add a new address record to the database"""
    with sqlite3.connect("address_book.db") as conn:
        c = conn.cursor()
        c.execute("""
        INSERT INTO addresses (first_name, last_name, address, city, state, zipcode)
        VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)
        """, {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })
        conn.commit()

    # Clear input fields
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    """Retrieve and display all records from the database"""
    mono_font = ('Courier', 12)  # Fixed-width font for alignment
    with sqlite3.connect("address_book.db") as conn:
        c = conn.cursor()
        c.execute("SELECT rowid, * FROM addresses")
        records = c.fetchall()

        print_records = ""
        for record in records:
            # Format: First Name, Last Name, Row ID
            print_records += f"{record[1]:<15} {record[2]:<15} {str(record[0]):>5}\n"

        # Display records in a Label
        record_label = Label(root, text=print_records, font=mono_font, justify='left', anchor='w')
        record_label.grid(row=8, column=0, columnspan=3, sticky='we', padx=10, pady=5)

def delete(name):
    """Delete a record by first name"""
    with sqlite3.connect("address_book.db") as conn:
        c = conn.cursor()
        c.execute("DELETE FROM addresses WHERE first_name=?", (name,))
        delete_entry.delete(0, END)
        conn.commit()

# -------------------------
# Step 3: Entry widgets for user input
# Entry parameters explained before in "03_entry_and_button.py": width
# Label parameters explained before in "02_labels_and_grid.py": text, anchor
f_name = Entry(root, width=30)
f_name.grid(row=0, column=2, padx=20)
Label(root, text="First Name", anchor=W).grid(row=0, column=0)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=2, padx=20)
Label(root, text="Last Name", anchor=W).grid(row=1, column=0)

address = Entry(root, width=30)
address.grid(row=2, column=2, padx=20)
Label(root, text="Address", anchor=W).grid(row=2, column=0)

city = Entry(root, width=30)
city.grid(row=3, column=2, padx=20)
Label(root, text="City", anchor=W).grid(row=3, column=0)

state = Entry(root, width=30)
state.grid(row=4, column=2, padx=20)
Label(root, text="State", anchor=W).grid(row=4, column=0)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=2, padx=20)
Label(root, text="Zipcode", anchor=W).grid(row=5, column=0)

delete_entry = Entry(root, width=30)
delete_entry.grid(row=9, column=2, padx=20)
Label(root, text="Name to delete").grid(row=9, column=0, pady=20)

# -------------------------
# Step 4: Buttons
# Button parameters explained before in "03_entry_and_button.py": text, command
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=6, column=0, columnspan=3, pady=10, sticky="we", padx=10)

query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=3, sticky="we", padx=10, pady=10)

delete_button = Button(root, text="Delete", command=lambda: delete(delete_entry.get()))
delete_button.grid(row=10, column=0, columnspan=3, sticky="we", padx=10, pady=10)

# -------------------------
# Step 5: Start Tkinter event loop
root.mainloop()
