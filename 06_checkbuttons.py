# 06_checkbuttons.py
# Demonstrates using CheckButtons for multiple selections

from tkinter import Tk, Label, Checkbutton, IntVar, Button, messagebox

# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("CheckButton Example")
root.geometry("300x200")

# Step 2: Label
# Parameters explained before in "01_hello_world.py"
label = Label(root, text="Select your hobbies:")
label.pack(pady=5)

# Step 3: Create IntVars to store checkbutton states
# IntVar explained before in "05_radio_buttons.py"
hobby1 = IntVar()
hobby2 = IntVar()
hobby3 = IntVar()

# Step 4: Create CheckButtons
# CheckButton parameters:
# - text: label for the button
# - variable: Tkinter variable linked to button
cb1 = Checkbutton(root, text="Reading", variable=hobby1)
cb2 = Checkbutton(root, text="Sports", variable=hobby2)
cb3 = Checkbutton(root, text="Gaming", variable=hobby3)

cb1.pack()
cb2.pack()
cb3.pack()

# Step 5: Button to show selections
# Button parameters explained before in "03_entry_and_button.py": text, command
def show_hobbies():
    selected = []
    if hobby1.get(): selected.append("Reading")
    if hobby2.get(): selected.append("Sports")
    if hobby3.get(): selected.append("Gaming")
    messagebox.showinfo("Selected Hobbies", ", ".join(selected))

submit_button = Button(root, text="Show Hobbies", command=show_hobbies)
submit_button.pack(pady=10)

# Step 6: Start Tkinter event loop
root.mainloop()
