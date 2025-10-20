# 08_scale_slider.py
# Demonstrates using Scale (slider) widget to select numeric values

from tkinter import Tk, Scale, Label

# Step 1: Create main window
# Parameters explained before in "01_hello_world.py"
root = Tk()
root.title("Scale Example")
root.geometry("300x150")

# Step 2: Label
# Parameters explained before in "01_hello_world.py"
label = Label(root, text="Select a value:")
label.pack(pady=5)

# Step 3: Create Scale
# Scale parameters:
# - from_: start value of scale
# - to: end value
# - orient: horizontal or vertical
# - length: length of the slider
scale = Scale(root, from_=0, to=100, orient="horizontal", length=200)
scale.pack(pady=10)

# Step 4: Start Tkinter event loop
root.mainloop()
