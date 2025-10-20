# 07_listbox.py
# Demonstrates using a Listbox widget to select items

from tkinter import Tk, Listbox, Button, messagebox

# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Listbox Example")
root.geometry("300x200")

# Step 2: Create Listbox
# Listbox parameters:
# - selectmode: "single" or "multiple"
# - height: number of visible rows
lb = Listbox(root, selectmode="multiple", height=5)
lb.pack(pady=10)

# Step 3: Insert items into Listbox
lb.insert(1, "Python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "JavaScript")

# Step 4: Button to show selected items
# Button parameters explained before in "03_entry_and_button.py": text, command
def show_selection():
    selection = [lb.get(i) for i in lb.curselection()]  # curselection() returns selected indices
    messagebox.showinfo("Selected Languages", ", ".join(selection))

btn = Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=5)

# Step 5: Start Tkinter event loop
root.mainloop()
