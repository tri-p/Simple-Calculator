# PABUNA, KATRINA B.

# Import tkinter GUI
from tkinter import *

# Define operation buttons

# Create the window for choosing an operation
calcu = Tk()
calcu.title("Simple Calculator - 2023")
calcu.geometry("470x200")
calcu.config(bg="light pink")

# Display the operation buttons
operations = ""

operation = Label(calcu, text="Choose an \noperation to use:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
operation.grid(row=0, column=0, padx=5, pady=10)

# create buttons for operations
add_button = Button(calcu, text="+", font=("helvetica", 20, "bold"))
add_button.grid(row=1, column=1, padx=5, pady=20)

sub_button = Button(calcu, text="-", font=("helvetica", 20, "bold"))
sub_button.grid(row=1, column=2, padx=5, pady=20)

mul_button = Button(calcu, text="*", font=("helvetica", 20, "bold"))
mul_button.grid(row=1, column=3, padx=5, pady=20)

div_button = Button(calcu, text="/", font=("helvetica", 20, "bold"))
div_button.grid(row=1, column=4, padx=5, pady=20)

# Ask user to input two numbers

# Evaluate the equation

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()