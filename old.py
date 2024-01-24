import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

current_input = "0"

root = tk.Tk()
root.title("Calculator")

label = ttk.Label(root, text=current_input, font=("Arial", 25))
label.grid(row=1, column=0, columnspan=100)

# parse_errors = {
#    "1": "First value was an operator.",
#    "2": "Double operators.",
#    "3": "Was expecting an operator.",
# }

operators = ["+", "-", "/", "x"]


def parse_input(input) -> list[str]:
    list = [""]
    current_index = 0
    for char in input:
        if char in operators:
            current_index = current_index + 1
        if len(list) - 1 < current_index:
            list.extend([""])
        list[current_index] = list[current_index] + char
        if char in operators:
            current_index = current_index + 1
    return list

def display_error(message: str):
    messagebox.showerror("Calculator: ERROR!", message)


def better_float(var: str) -> float | None:
    value = None
    try:
        value = float(var)
    except:
        value = None
    return value

'''
def correct_order(list: list[str]) -> list[str]:
    priority = {"x": 3, "/": 2, "-": 1, "+": 1}
    new_list = []
    new_list.extend(list)
    list_of_operators = []
    for index in range(0, len(list)):
        is_operator = not (index % 2) == 0
        value = list[index]
        if is_operator:
            list_of_operators.append(value)
    def sort_function(operator):
        return priority[operator]
    list_of_operators.sort(key=sort_function, reverse=True)
    operator_index = -1
    for index in range(0, len(list)):
        is_operator = not (index % 2) == 0
        value = list[index]
        if is_operator:
            operator_index = operator_index + 1
            new_list[index] = list_of_operators[operator_index]
            right = new_list[index + 1]
            left = new_list[-(index + 1)]
            new_list[-(index + 1)] = right
            new_list[index + 1] = left
    return new_list
'''

'''
def parse():
    global current_input
   
    operations_priory = {"x": 2, "/": 2, "-": 1, "+": 1}
    
    input = parse_input(current_input)
    
    if not len(input) > 1:
        return display_error("No operations provided!")

    total = better_float(input[0])
    if total == None:
        return display_error(f"{input[0]} is not a valid number.")

    if input[len(input) - 1] in operators:
        return display_error(f"Last value cannot be an operation other then equal.")

    last_operator = input[1]
    for index in range(2, len(input)):
        is_operator = not (index % 2) == 0
        value = input[index]
        if is_operator:
            last_operator = value
        else:
            number = better_float(value)
            if number == None:
                return display_error(f"{value} is not a valid number.")
            if last_operator == "+":
                total = total + number
            elif last_operator == "-":
                total = total - number
            elif last_operator == "/":
                total = total / number
            elif last_operator == "x":
                total = total * number

    if str(total).endswith(".0"):
        total = str(total).replace(".0", "")

    current_input = str(total)
    label.configure(text=current_input)
    return
'''

def parse():
    global current_input
   
    operations_priority = {"x": 2, "/": 2, "-": 1, "+": 1}
    
    input = parse_input(current_input)
    
    if not len(input) > 1:
        return display_error("No operations provided!")

    if input[len(input) - 1] in operators:
        return display_error("Last value cannot be an operation other then equal.")

    def do_math(list: list[str]) -> float:
        solver_index = 0
        last_priority = 0
        for index in range(0, len(list)):
            if not (index % 2) == 0:
                priority = operations_priority[list[index]]
                if priority > last_priority:
                    last_priority = priority
                    solver_index = index
        if solver_index == 0: return list[0]
        operator = list[solver_index]
        result = 0
        first_number = better_float(list[solver_index - 1])
        second_number = better_float(list[solver_index + 1])
        if first_number == None:
            return display_error(f"{first_number} is not a valid number.")
        if second_number == None:
            return display_error(f"{second_number} is not a valid number.")
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "/":
            result = first_number / second_number
        elif operator == "x":
            result = first_number * second_number
        list[solver_index - 1] = result
        list.pop(solver_index)
        list.pop(solver_index)
        
        return do_math(list)

    total = do_math(input)        

    if str(total).endswith(".0"):
        total = str(total).replace(".0", "")

    current_input = str(total)
    label.configure(text=current_input)
    return


def input_char(char: str):
    if char == "=":
        return parse()
    global current_input
    if char in operators:
        last_char = current_input[-1]
        if last_char in operators:
            return
    if current_input == "0":
        current_input = ""
    current_input = current_input + char
    label.configure(text=current_input)
    if current_input[0] in operators:
        current_input = "0"
        label.configure(text=current_input)


def _backspace():
    global current_input
    if current_input == "0":
        return
    current_input = current_input[:-1]
    if current_input == "":
        current_input = "0"
    label.configure(text=current_input)


def _7():
    input_char("7")


def _8():
    input_char("8")


def _9():
    input_char("9")


def _4():
    input_char("4")


def _5():
    input_char("5")


def _6():
    input_char("6")


def _1():
    input_char("1")


def _2():
    input_char("2")


def _3():
    input_char("3")


def _0():
    input_char("0")


def _dot():
    input_char(".")


def _equal():
    input_char("=")


def _add():
    input_char("+")


def _subtract():
    input_char("-")


def _divide():
    input_char("/")


def _multiplication():
    input_char("x")


ttk.Button(root, text="7", command=_7).grid(row=2, column=0)
ttk.Button(root, text="8", command=_8).grid(row=2, column=1)
ttk.Button(root, text="9", command=_9).grid(row=2, column=2)
ttk.Button(root, text="4", command=_4).grid(row=3, column=0)
ttk.Button(root, text="5", command=_5).grid(row=3, column=1)
ttk.Button(root, text="6", command=_6).grid(row=3, column=2)
ttk.Button(root, text="1", command=_1).grid(row=4, column=0)
ttk.Button(root, text="2", command=_2).grid(row=4, column=1)
ttk.Button(root, text="3", command=_3).grid(row=4, column=2)
ttk.Button(root, text="0", command=_0).grid(row=5, column=1)
ttk.Button(root, text="/", command=_divide).grid(row=2, column=3)
ttk.Button(root, text="x", command=_multiplication).grid(row=3, column=3)
ttk.Button(root, text="-", command=_subtract).grid(row=4, column=3)
ttk.Button(root, text="+", command=_add).grid(row=5, column=3)
ttk.Button(root, text="=", command=_equal).grid(row=5, column=2)
ttk.Button(root, text=".", command=_dot).grid(row=5, column=0)
ttk.Button(root, text="Backspace", command=_backspace).grid(
    row=6, column=0, columnspan=4
)


"""
ttk.Label(root, text="----------------------------------------").grid(
    row=7, column=0, columnspan=4
)
ttk.Label(root, text="Errors", font=("Arial", 25)).grid(row=8, column=0, columnspan=4)

last_error_row = 8
for key in parse_errors:
    last_error_row = last_error_row + 1
    ttk.Label(root, text=f"{key} - {parse_errors[key]}", font=("Arial", 12)).grid(
        row=last_error_row, column=0, columnspan=4
    )
"""

root.mainloop()
