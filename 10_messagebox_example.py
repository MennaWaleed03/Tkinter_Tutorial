# 10_messagebox_example.py

# Demonstrates different types of Tkinter messageboxes, including askyesno, askokcancel, askretrycancel, showinfo, showwarning , showerror

from tkinter import Tk, Button, messagebox

# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Advanced Messagebox Example")
root.geometry("400x300")

# -------------------------
# Step 2: Functions to show different messageboxes
# messagebox functions:
# - showinfo(title, message): informational popup
# - showwarning(title, message): warning popup
# - showerror(title, message): error popup
# - askquestion(title, message): returns "yes" or "no"
# - askokcancel(title, message): returns True or False
# - askyesno(title, message): returns True or False
# - askretrycancel(title, message): returns True or False

def show_info():
    messagebox.showinfo("Info", "This is an information message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question_example():
    result = messagebox.askquestion("Question", "Do you like Python?")
    # askquestion() returns string: "yes" or "no"
    messagebox.showinfo("Response", f"You answered: {result}")

def ask_ok_cancel_example():
    result = messagebox.askokcancel("OK/Cancel", "Do you want to proceed?")
    # askokcancel() returns boolean: True if OK, False if Cancel
    messagebox.showinfo("Response", f"Result: {result}")

def ask_yes_no_example():
    result = messagebox.askyesno("Yes/No", "Do you want to continue?")
    # askyesno() returns boolean: True if Yes, False if No
    messagebox.showinfo("Response", f"Result: {result}")

def ask_retry_cancel_example():
    result = messagebox.askretrycancel("Retry/Cancel", "Operation failed. Retry?")
    # askretrycancel() returns boolean: True if Retry, False if Cancel
    messagebox.showinfo("Response", f"Result: {result}")

# -------------------------
# Step 3: Buttons to trigger each messagebox
# Button parameters explained before in "03_entry_and_button.py": text, command
Button(root, text="Show Info", command=show_info).pack(pady=5)
Button(root, text="Show Warning", command=show_warning).pack(pady=5)
Button(root, text="Show Error", command=show_error).pack(pady=5)
Button(root, text="Ask Question", command=ask_question_example).pack(pady=5)
Button(root, text="Ask OK/Cancel", command=ask_ok_cancel_example).pack(pady=5)
Button(root, text="Ask Yes/No", command=ask_yes_no_example).pack(pady=5)
Button(root, text="Ask Retry/Cancel", command=ask_retry_cancel_example).pack(pady=5)

# -------------------------
# Step 4: Start Tkinter event loop
root.mainloop()