# PABUNA, KATRINA B.

# Import tkinter GUI
from tkinter import *

# Disable all entry buttons
def disable():
    add_button.config(state=DISABLED)
    sub_button.config(state=DISABLED)
    mul_button.config(state=DISABLED)
    div_button.config(state=DISABLED)
    first_num_box.config(state=DISABLED)
    sec_num_box.config(state=DISABLED)

# Define operation buttons
def addition():
    try:
        first_num = int(first_num_box.get())
        sec_num = int(sec_num_box.get())
    except ValueError:
        output_disp.config(text="Error: Invalid input")
        disable()
        ask()
        return
    output_disp.config(text=str(first_num) + " + " + str(sec_num) + " = " + str(first_num + sec_num))
    disable()
    ask()

def subtraction():
    try:
        first_num = int(first_num_box.get())
        sec_num = int(sec_num_box.get())
    except ValueError:
        output_disp.config(text="Error: Invalid input")
        disable()
        ask()
        return
    output_disp.config(text=str(first_num) + " - " + str(sec_num) + " = " + str(first_num - sec_num))
    disable()
    ask()

def multiplication():
    try:
        first_num = int(first_num_box.get())
        sec_num = int(sec_num_box.get())
    except ValueError:
        output_disp.config(text="Error: Invalid input")
        disable()
        ask()
        return
    output_disp.config(text=str(first_num) + " * " + str(sec_num) + " = " + str(first_num * sec_num))
    disable()
    ask()

def division():
    try:
        first_num = int(first_num_box.get())
        sec_num = int(sec_num_box.get())
        output_disp.config(text=str(first_num) + " / " + str(sec_num) + " = " + str(first_num / sec_num))
        disable()
        ask()
        if sec_num == 0:
            raise ZeroDivisionError()
    except ZeroDivisionError:
        output_disp.config(text="Error: Division by zero")
        disable()
        ask()
    except ValueError:
        output_disp.config(text="Error: Invalid input")
        disable()
        return
    disable()
    ask()

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
add_button = Button(calcu, text="+", font=("helvetica", 20, "bold"), command=addition)
add_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

sub_button = Button(calcu, text="-", font=("helvetica", 20, "bold"), command=subtraction)
sub_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

mul_button = Button(calcu, text="*", font=("helvetica", 20, "bold"), command=multiplication)
mul_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

div_button = Button(calcu, text="/", font=("helvetica", 20, "bold"), command=division)
div_button.pack(side=LEFT, padx=5, pady=20, anchor='n')

# Display the output
output_disp = Label(calcu, text="", fg="white", bg="light pink", font=("helvetica", 25, "bold"), width=25)
output_disp.place(x=5, y=360)

# Create a popup window for another calculation
# function to ask if the user wants to try again
def ask():
    ask = Toplevel()
    ask.title("Try Again?")
    ask.config(bg="light pink")
    ask.resizable(False, False)

    # create a label asking if the user wants to try again
    ask_label = Label(ask, text="Would you like to try again?", bg="light pink", font=("helvetica", 12, "bold"))
    ask_label.pack(padx=10, pady=10)
    
    # create a frame to hold the buttons
    button_frame = Frame(ask, bg="light pink")
    button_frame.pack(padx=10, pady=10)

    # create a "Yes" button that returns True
    yes_button = Button(button_frame, text="Yes", font=("helvetica", 12, "bold"))
    yes_button.pack(padx=5, pady=5)

    # create a "No" button that returns False
    no_button = Button(button_frame, text="No", font=("helvetica", 12, "bold"))
    no_button.pack(padx=5, pady=5)

    # ===== start popup window =====
    ask.mainloop()


# Create a popup window to exit the app

# ===== start =====
calcu.mainloop()