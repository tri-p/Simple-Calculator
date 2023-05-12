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
                 bg="light pink", fg="black")
operation_input.pack(padx=5, pady=10)

# display the input
def op_display():
    operation_disp.config("Operation is: " + operations.get())

# create buttons for operations
add_button = Button(calcu, text="+", font=("helvetica", 20, "bold"), command=lambda: func_op("+"))
add_button.pack(side=LEFT, padx=5, pady=20)

sub_button = Button(calcu, text="-", font=("helvetica", 20, "bold"), command=lambda: func_op("-"))
sub_button.pack(side=LEFT, padx=5, pady=20)

mul_button = Button(calcu, text="*", font=("helvetica", 20, "bold"), command=lambda: func_op("*"))
mul_button.pack(side=LEFT, padx=5, pady=20)

div_button = Button(calcu, text="/", font=("helvetica", 20, "bold"), command=lambda: func_op("/"))
div_button.pack(side=LEFT, padx=5, pady=20)

# display the input
operation_disp = Label(calcu, textvariable=operations, fg="white", bg="light pink", font=("helvetica", 12))
operation_disp.pack(padx=5, pady=10)

# Ask user to input two numbers
first_num = IntVar()
second_num = IntVar()

input_num = Label(calcu, text="Input two numbers:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
input_num.pack(padx=5, pady=10)

first_num_label = Label(calcu, text="Input first number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
first_num_label.pack(padx=5, pady=10)

sec_num_label = Label(calcu, text="Input second number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
sec_num_label.pack(padx=5, pady=10)

first_num_box = Entry(calcu, textvariable=first_num, fg="black", font=("helvetica", 10, "bold"))
first_num_box.pack(padx=5, pady=10)

sec_num_box = Entry(calcu, textvariable=second_num, fg="black", font=("helvetica", 10, "bold"))
sec_num_box.pack(padx=5, pady=10)

# Evaluate the equation
answer = ""

def calculate():

    try:
        global operation
        answer_display.setvar(operation)
        equal= str(eval(first_num, operation, second_num))
        answer_display.setvar(equal)
        answer = ""

    except:
        answer_display.config(text="Error")
        
# calculate button
calcu_button = Button(calcu, text="Calculate", fg="black", font=("helvetica", 12, "bold"), command=calculate)
calcu_button.pack(padx=5, pady=10)

answer_display = Label(calcu, textvariable=answer, fg="white", bg="light pink", font=("helvetica", 12,"bold"))
answer_display.pack(padx=5, pady=10)

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()