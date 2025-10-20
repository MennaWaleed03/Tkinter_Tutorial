# 13_simple_calculator.py
# A simple calculator using Tkinter with basic arithmetic operations

from tkinter import Tk, Entry, Button, END
import re  # Regular expressions used to split arithmetic expressions

# -------------------------
# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Simple Calculator")

# Step 2: Entry widget for input/output
# Entry parameters explained before in "03_entry_and_button.py": width
e = Entry(root)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="we")  
# sticky="we": makes the widget expand horizontally

# -------------------------
# Step 3: Helper functions

def convert_to_int(n):
    """Convert string to integer, show ERROR if invalid"""
    try:
        x = int(n)
    except:
        e.insert(0, "ERROR")
        raise ValueError
    return x

def onclick(number):
    """Handle button clicks"""
    current = e.get()
    
    if number == "Clear":
        e.delete(0, END)
        return
    
    if number == "del":
        e.delete(len(current)-1, END)
        return
    
    elif number == "=":
        e.delete(0, END)
        # Split expression into numbers and operators
        eq = re.split(r'(?=[+-/*])|(?<=[+-/*])', current)
        res = int(eq[0])
        
        for i in range(len(eq)-1):
            if eq[i] == '+':
                res += convert_to_int(eq[i+1])
            elif eq[i] == '-':
                res -= convert_to_int(eq[i+1])
            elif eq[i] == '*':
                res *= convert_to_int(eq[i+1])
            elif eq[i] == '/':
                try:
                    res = round(res / convert_to_int(eq[i+1]), 5)
                except:
                    e.insert(0, "ERROR")
                    raise ZeroDivisionError
        
        e.insert(0, res)
        return
    
    else:
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

# -------------------------
# Step 4: Button creation

def create_button(number):
    """Return a Button with given number/operator"""
    # Button parameters explained before in "03_entry_and_button.py": text, command
    # New parameters:
    # - padx, pady: internal padding inside button
    return Button(root, text=number, padx=40, pady=20, command=lambda: onclick(number))

# -------------------------
# Step 5: Create number buttons
numbers = [str(i) for i in range(10)]
r = 1
c = 0
for n in numbers:
    button = create_button(n)
    button.grid(row=r, column=c, padx=5)
    c += 1
    if c % 3 == 0:
        r += 1
        c = 0

# -------------------------
# Step 6: Create operator buttons
clear_button = create_button("Clear")
add_button = create_button("+")
sub_button = create_button('-')
mul_button = create_button('*')
div_button = create_button("/")
equal_button = create_button("=")
del_button = create_button('del')

# Place operator buttons using grid
clear_button.grid(row=5, column=1, columnspan=2, sticky="we", padx=5, pady=5)
add_button.grid(row=5, column=0)
sub_button.grid(row=4, column=1)
mul_button.grid(row=6, column=0)
div_button.grid(row=6, column=1)
equal_button.grid(row=4, column=2, padx=5)
del_button.grid(row=6, column=2)

# Exit button
# Button parameters explained before in "03_entry_and_button.py": text, command
exit_button = Button(root, text="Exit", command=root.quit, borderwidth=10)
exit_button.grid(row=7, column=0, columnspan=3, sticky="we", pady=10)

# -------------------------
# Step 7: Bind keyboard input
# root.bind(event, function): bind a key event to a function
root.bind("<Key>", lambda event: onclick(event.char))

# Step 8: Start Tkinter event loop
root.mainloop()