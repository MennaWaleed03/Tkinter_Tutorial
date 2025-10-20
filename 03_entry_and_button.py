# 03_entry_and_button.py
# Shows how to get input using Entry widget and a Button

from tkinter import Tk, Label, Entry, Button, messagebox

# Step 1: Create the main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Entry and Button Example")
root.geometry("300x150")

# Step 2: Create a Label
# Parameters explained before in "01_hello_world.py"
label = Label(root, text="Enter your name:")
label.pack(pady=5)

# Step 3: Create an Entry widget
# Entry parameters:
# - width: width of the input field
name_entry = Entry(root, width=25)
name_entry.pack(pady=5)

# Step 4: Define a function for the Button click
def greet_user():
    # get(): retrieves text from Entry (new concept)
    name = name_entry.get()
    if name.strip():
        # messagebox.showinfo(title, message): displays info popup
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        # messagebox.showwarning(title, message): displays warning popup
        messagebox.showwarning("Warning", "Please enter your name.")

# Step 5: Create a Button widget
# Button parameters:
# - text: text displayed on button
# - command: function to run when clicked
greet_button = Button(root, text="Greet Me", command=greet_user)
greet_button.pack(pady=10)

# Step 6: Start Tkinter event loop
root.mainloop()
