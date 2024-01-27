# A stylized calculator created by Jacob Humston


######################### Modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import re


######################### Static Variables
button_characters = [
    "Next",
    "Previous",
    "Back",
    "Clear",
    "(",
    ")",
    "%",
    "/",
    "7",
    "8",
    "9",
    "*",
    "4",
    "5",
    "6",
    "+",
    "1",
    "2",
    "3",
    "—",
    "-",
    "0",
    ".",
    "=",
]
operators = ["%", "/", "*", "—", "+"]
operators_priority = {"%": 2, "/": 2, "*": 2, "—": 1, "+": 1}

######################### Create the main window.
window = tk.Tk()
window.title("Calculator")
window.iconphoto(False, tk.PhotoImage(file="assets/icon.png"))
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.resizable(width=False, height=False)


######################### Utility functions.
# Display an error popup.
def display_error(message: str) -> None:
    messagebox.showerror("Calculator | ERROR!", message)
    return None


# Convert a float to a string safely.
def better_float(var: str) -> float | None:
    value = None
    try:
        value = float(var)
    except:
        value = None
    return value


# Modify a number string to be displayed.
def modify_equation_string(string: str) -> str:
    new_string = string
    new_string = re.sub("(.{15})", "\\1\n", new_string, 0, re.DOTALL)
    new_string = new_string.removesuffix(".0")
    for operator in operators:
        new_string = new_string.replace(operator, f" {operator} ")
    return new_string


######################### Create the button frame.
main_frame = ttk.Frame(window)
main_frame.grid(row=1, column=0, columnspan=8)
main_frame.configure(border=10)


######################### Create the text label.
label = ttk.Label(main_frame, width=20)
label.grid(row=0, column=0, columnspan=8)
label.configure(padding=10, font=("Arial", 20))


######################### Function to add a character to the current label.
current_equation = "0"
equation_history = []


# Add a character to the equation.
def add_character_to_equation(character: str) -> None:
    global current_equation
    if current_equation == "0":
        current_equation = ""
    current_equation = f"{current_equation}{character}"
    label.configure(text=modify_equation_string(current_equation))
    return None


######################### Create buttons.
# Function to create the calculator buttons.
def create_buttons():
    column_index = 0
    last_row = -1

    for index, character in enumerate(button_characters):
        row = math.floor(index / 4) + 1
        if last_row != row:
            column_index = 0
        last_row = row
        column_index = column_index + 1
        column = column_index

        def command_function(character=character):
            add_character_to_equation(character)

        button = ttk.Button(main_frame, text=character, command=command_function)
        button.grid(row=row, column=column, sticky="nesw")

        if character == "":
            button.grid_remove()


create_buttons()  # Create the calculator buttons.


######################### Start the process.
window.mainloop()
