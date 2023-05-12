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

calcu_width = 500
calcu_height = 450

# get the screen witdth and height
screen_width = calcu.winfo_screenwidth()
screen_height = calcu.winfo_screenheight()

# calculate the x and y coordinates to center the window
x_coor = (screen_width // 2) - (calcu_width // 2)
y_coor = (screen_height // 2) - (calcu_height // 2)

# set the geometry of the window to center the texts
calcu.geometry("{}x{}+{}+{}".format(calcu_width, calcu_height, x_coor, y_coor))

# Ask user to input two numbers
input_num = Label(calcu, text="Input two numbers:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black")
input_num.pack(padx=5, pady=10)

first_num_label = Label(calcu, text="Input first number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
first_num_label.pack(padx=5, pady=10)

first_num_box = Entry(calcu, fg="black", font=("helvetica", 10, "bold"))
first_num_box.pack(padx=5, pady=10, anchor='n')

sec_num_label = Label(calcu, text="Input second number:", font=("helvetica", 10, "bold"),
                 bg="light pink", fg="black", justify=LEFT)
sec_num_label.pack(padx=5, pady=10)

sec_num_box = Entry(calcu, fg="black", font=("helvetica", 10, "bold"))
sec_num_box.pack(padx=5, pady=10, anchor='n')

# Display the operation buttons
operation_input = Label(calcu, text="Choose an \noperation to use:", font=("helvetica", 12, "bold"),
                 bg="light pink", fg="black")
operation_input.pack(padx=5, pady=10)

# create empty labels to center the buttons
Label(calcu, text="", bg="light pink").pack(side=LEFT, padx=75)

# create buttons for operations
add_button = Button(calcu, text="+", font=("helvetica", 20, "bold"), command=lambda: func_op("+"))
add_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

sub_button = Button(calcu, text="-", font=("helvetica", 20, "bold"), command=lambda: func_op("-"))
sub_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

mul_button = Button(calcu, text="*", font=("helvetica", 20, "bold"), command=lambda: func_op("*"))
mul_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

div_button = Button(calcu, text="/", font=("helvetica", 20, "bold"), command=lambda: func_op("/"))
div_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

# display the input
operation_disp = Label(calcu, fg="white", bg="light pink", font=("helvetica", 12))
operation_disp.pack(padx=5, pady=10)

# Create a popup window for another calculation

# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()