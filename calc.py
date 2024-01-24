# A stylized calculator created by Jacob Humston


######################### Modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


######################### Static Variables
characters = [
    "%BACK",
    "%CLEAR",
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
    "-",
    ".",
    "0",
    "",
    "=",
]


######################### Create the main window.
window = tk.Tk()
window.title("Calculator")
window.iconphoto(False, tk.PhotoImage(file="assets/icon.png"))


######################### Utility functions.
def display_error(message: str) -> None:
    messagebox.showerror("Calculator | ERROR!", message)
    return None


######################### Start the process.
window.mainloop()
