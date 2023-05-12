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
calcu.geometry("500x450")
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
first_num = IntVar()
second_num = IntVar()

input_num = Label(calcu, text="Input two numbers:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
input_num.grid(row=3, column=0, padx=5, pady=10)

first_num_label = Label(calcu, text="Input first number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
first_num_label.grid(row=4, column=0, pady=5)

sec_num_label = Label(calcu, text="Input second number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
sec_num_label.grid(row=6, column=0, pady=5)

first_num_box = Entry(calcu, textvariable=first_num, fg="black", font=("helvetica", 10, "bold"))
first_num_box.grid(row=5, column=0, padx=5, pady=5)

sec_num_box = Entry(calcu, textvariable=second_num, fg="black", font=("helvetica", 10, "bold"))
sec_num_box.grid(row=7, column=0, padx=5, pady=5)

# Evaluate the equation
answer = ""

def calculate():

    try:
        global operation
        equal= str(eval(first_num, operation, second_num))
        answer_display.setvar(equal)
        answer = ""

    except:
        answer_display.config(text="Error")
        
# calculate button
calcu_button = Button(calcu, text="Calculate", fg="black", font=("helvetica", 12, "bold"), command=calculate)
calcu_button.grid(row=8, column=0, padx=5, pady=10)

answer_display = Label(calcu, textvariable=answer, fg="white", bg="light pink", font=("helvetica", 12,"bold"))
answer_display.grid(row=9, column=0, padx=5, pady=10)

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()