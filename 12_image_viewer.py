# 14_image_viewer.py
# A simple Image Viewer using Tkinter and PIL (Pillow)

from tkinter import Tk, Label, Button, SUNKEN, W
from PIL import ImageTk, Image  # PIL is used to open and resize images

# -------------------------
# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Image Viewer APP")

# -------------------------
# Step 2: Load images
# ImageTk.PhotoImage(Image.open("file").resize((width,height)))
# - Image.open(): opens an image file
# - resize(): changes image size
# - ImageTk.PhotoImage(): converts image for Tkinter Label
my_image1 = ImageTk.PhotoImage(Image.open("my_pic.jpg").resize((400, 400)))
my_image2 = ImageTk.PhotoImage(Image.open("Menna Waleed.jpg").resize((400, 400)))
my_image3 = ImageTk.PhotoImage(Image.open("pic.jpg").resize((400, 400)))

# Store images in a list for easy navigation
image_list = [my_image1, my_image2, my_image3]
length = len(image_list)  # Total number of images
index = 0  # Current image index

# -------------------------
# Step 3: Display first image in a Label
# Label parameters explained before in "02_labels_and_grid.py": text, bg
label = Label(image=image_list[index])
label.grid(row=0, column=0, columnspan=3, sticky="we")  
# sticky="we": stretch the label horizontally

# -------------------------
# Step 4: Status bar to show current image number
# Label parameters explained before
status = Label(root, text=f"Image {index+1} of {length}", bd=1, relief=SUNKEN, pady=10, anchor=W)
# bd: border width
# relief: border style (SUNKEN creates a recessed look)
# pady: vertical padding inside label
# anchor=W: text alignment to the west (left)
status.grid(row=2, column=0, columnspan=3, sticky="we")

# -------------------------
# Step 5: Navigation function
def onclick(symbol):
    """Navigate through images"""
    global index, label, status

    if symbol == "=>":
        index = (index + 1) % length  # Go to next image, wrap around
    if symbol == "<=":
        index = (index - 1) % length  # Go to previous image, wrap around

    # Remove previous image and status
    label.grid_forget()
    status.grid_forget()

    # Update label with new image
    label = Label(image=image_list[index])
    label.grid(row=0, column=0, columnspan=3, sticky="we")

    # Update status bar
    status = Label(root, text=f"Image {index+1} of {length}", bd=1, relief=SUNKEN, pady=10, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky="we")

# -------------------------
# Step 6: Buttons
# Button parameters explained before in "03_entry_and_button.py": text, command
# New parameters:
# - padx, pady: internal padding inside button
button_next = Button(root, text="=>", command=lambda: onclick("=>"), padx=10, pady=10)
button_prev = Button(root, text="<=", command=lambda: onclick("<="), padx=10, pady=10)
exit_button = Button(root, text="Exit", command=quit, padx=10, pady=10)

# Place buttons using grid
button_prev.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
button_next.grid(row=1, column=2)

# -------------------------
# Step 7: Start Tkinter event loop
root.mainloop()
