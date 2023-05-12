# PABUNA, KATRINA B.

# Import tkinter GUI
from tkinter import *

# Define operation buttons
operation = ""
def func_op(number):
    global operation
    operation = operation + str(number)
    operations.set(operation)

# Create the window for choosing an operation
calcu = Tk()
calcu.title("Simple Calculator - 2023")
calcu.geometry("470x200")
calcu.config(bg="light pink")

# Display the operation buttons
operations = StringVar()

operation_input = Label(calcu, text="Choose an \noperation to use:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
operation_input.grid(row=0, column=0, padx=5, pady=10)

# display the input
def op_display():
    operation_disp.config("Operation is: " + operations.get())

# create buttons for operations
add_button = Button(calcu, text="+", font=("helvetica", 20, "bold"), command=lambda: func_op("+"))
add_button.grid(row=1, column=1, padx=5, pady=20)

sub_button = Button(calcu, text="-", font=("helvetica", 20, "bold"), command=lambda: func_op("-"))
sub_button.grid(row=1, column=2, padx=5, pady=20)

mul_button = Button(calcu, text="*", font=("helvetica", 20, "bold"), command=lambda: func_op("*"))
mul_button.grid(row=1, column=3, padx=5, pady=20)

div_button = Button(calcu, text="/", font=("helvetica", 20, "bold"), command=lambda: func_op("/"))
div_button.grid(row=1, column=4, padx=5, pady=20)

# display the input
operation_disp = Label(calcu, textvariable=operations, fg="white", bg="light pink", font=("helvetica", 12))
operation_disp.grid(row=2, column=1, sticky=W)

# Ask user to input two numbers

# Evaluate the equation

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()