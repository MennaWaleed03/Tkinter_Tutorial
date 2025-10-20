# 02_labels_and_grid.py
# Demonstrates multiple Labels using grid layout

from tkinter import Tk, Label

# Step 1: Create the main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Grid Example")
root.geometry("300x150")

# Step 2: Explain new Label/grid parameters not explained before
# grid() parameters:
# - row: row index in the grid
# - column: column index in the grid
# - columnspan: number of columns the widget should span
# - padx, pady: padding around the widget
# Label parameters explained before in "01_hello_world.py": text, font, bg, width

# Step 3: Create Labels
label1 = Label(root, text="Label 1", bg="lightblue", width=10)
label2 = Label(root, text="Label 2", bg="lightgreen", width=10)
label3 = Label(root, text="Label 3", bg="lightyellow", width=10)

# Step 4: Place Labels using grid (parameters explained above)
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Step 5: Start Tkinter event loop
root.mainloop()
