# 04_button_expand.py
# Demonstrates how a Button can expand to fill available space

from tkinter import Tk, Button

# Step 1: Create the main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Button Expand Example")
root.geometry("300x150")

# Step 2: Create a Button
# Button parameters explained before in "03_entry_and_button.py": text, command
# New parameter:
# - expand: makes the widget expand to fill extra space in pack()
# - fill: specifies which direction to fill (X, Y, or BOTH)
def on_click():
    print("Button clicked!")

expand_button = Button(root, text="Click Me", command=on_click)
expand_button.pack(expand=True, fill="both", padx=10, pady=10)  # fill both horizontally and vertically

# Step 3: Start Tkinter event loop
root.mainloop()
