# 15_file_dialog.py
# Demonstrates using Tkinter file dialogs to open an image

from tkinter import Tk, Button, Label, filedialog
from PIL import ImageTk, Image  # PIL used to open and resize images

# -------------------------
# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("File Dialog Example")

# -------------------------
# Step 2: Define function to open file
def open_file():
    """Open an image file using a file dialog and display it"""
    global my_img  # Keep a reference to avoid garbage collection

    # filedialog.askopenfilename parameters:
    # - initialdir: starting folder
    # - title: dialog title
    # - filetypes: tuple of (label, pattern) to filter file types
    filename = filedialog.askopenfilename(
        initialdir=r"C:\Users\mewal\OneDrive\Pictures\Saved Pictures",
        title="Select a file",
        filetypes=(
            ("PNG files", "*.png *.PNG"),
            ("JPG files", "*.jpg *.JPG"),
            ("All files", "*.*")
        )
    )

    if filename:  # If a file was selected
        # Open and resize image
        my_img = ImageTk.PhotoImage(Image.open(filename).resize((250, 250)))
        # Display image in a Label
        Label(root, image=my_img).pack()

# -------------------------
# Step 3: Button to trigger file dialog
# Button parameters explained before in "03_entry_and_button.py": text, command
Button(root, text="Select Photo", command=open_file).pack(pady=10)

# -------------------------
# Step 4: Start Tkinter event loop
root.mainloop()
