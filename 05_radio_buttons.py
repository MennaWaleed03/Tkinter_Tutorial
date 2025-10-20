# 05_radio_buttons.py
# Demonstrates using RadioButtons for selecting options

from tkinter import Tk, Label, Radiobutton, IntVar

# Step 1: Create the main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Radio Button Example")
root.geometry("300x200")

# Step 2: Label (parameters explained before in "01_hello_world.py")
label = Label(root, text="Choose an option:")
label.pack(pady=5)

# Step 3: Create an IntVar to store the selected value
# IntVar(): a variable class that stores integer values for Tkinter widgets
selected_option = IntVar()
selected_option.set(1)  # Set default value

# Step 4: Create RadioButtons
# RadioButton parameters:
# - text: label shown next to button
# - variable: Tkinter variable linked to the button
# - value: value assigned if this option is selected
r1 = Radiobutton(root, text="Option 1", variable=selected_option, value=1)
r2 = Radiobutton(root, text="Option 2", variable=selected_option, value=2)
r3 = Radiobutton(root, text="Option 3", variable=selected_option, value=3)

r1.pack()
r2.pack()
r3.pack()

# Step 5: Start Tkinter event loop
root.mainloop()
