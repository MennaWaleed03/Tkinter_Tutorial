# 01_hello_world.py
# A basic Tkinter example: create a window and display "Hello, World!"

from tkinter import Tk, Label

# Step 1: Create the main window
# Tk() creates the main application window
# title(): sets the window title
# geometry(): sets window size (width x height)
root = Tk()
root.title("Hello World App")
root.geometry("300x100")

# Step 2: Create a Label widget
# Label parameters:
# - text: the text to display
# - font: tuple specifying font type and size
hello_label = Label(root, text="Hello, World!", font=("Arial", 16))
hello_label.pack(pady=20)  # pack(): places the widget; pady adds vertical padding

# Step 3: Start the Tkinter event loop
root.mainloop()  # Keeps the window open and responsive
