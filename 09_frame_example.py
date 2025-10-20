# 09_frame_example.py
# Demonstrates using Frame to group widgets

from tkinter import Tk, Frame, Label, Button

# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Frame Example")
root.geometry("300x200")

# Step 2: Create Frame
# Frame parameters:
# - bg: background color (explained in "02_labels_and_grid.py")
# - width, height: size of the frame
frame = Frame(root, bg="lightgray", width=250, height=150)
frame.pack(pady=10)

# Step 3: Add widgets inside Frame
label = Label(frame, text="Inside Frame", bg="lightgray")  # Label params explained before
label.place(x=70, y=20)  # place(): new geometry manager, positions widgets by x,y coordinates
btn = Button(frame, text="Click Me")  # Button params explained before
btn.place(x=90, y=60)

# Step 4: Start Tkinter event loop
root.mainloop()
