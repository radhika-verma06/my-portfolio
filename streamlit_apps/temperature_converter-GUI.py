#temperature_converte

import re

def cel_to_far(temp_C):
    return (temp_C * 9/5) + 32

def far_to_cel(temp_F):
    return(temp_F - 32)*5/9

def valid_input(user_input):
    pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)$'

    return bool(re.match(pattern, user_input))

print("🌡️ Welcome to the Temperature Converter!")
print("You can convert:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("Type 'exit' anytime to quit.\n")

while True:
    choice = input("choose conversion 1 or 2").strip()

    if choice.lower() == "exit":
        print("goodbye")
        break
    if choice not in ['1' , '2']:
        print(f"enter a valid input. {choice} is invalid ")
        continue

    while True:
        temp_input = input("Enter the temperature you want to convert: ").strip()

        if temp_input.lower() == "exit":
            print("Goodbye!")
            break

        if not temp_input:
            print("Input cannot be empty. Please enter a valid number (integer or decimal).\n")
            continue

        if not valid_input(temp_input):
            print("❌ Invalid input. Please enter a valid number (integers or decimals).\n")
            continue
        break

    temperature = float(temp_input)

    if choice == '1':
        converted = cel_to_far(temperature)
        print(f"{temperature} is equal to {converted:.2f}F")

    if choice == '2':
        converted = far_to_cel(temperature)
        print(f"{temperature} is equal to {converted:.2f}C")
        """


import re
import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(temp_C):
    return (temp_C * 9/5) + 32

def fahrenheit_to_celsius(temp_F):
    return (temp_F - 32) * 5/9

def is_valid_number(user_input):
    
    Check if input is a valid integer or float (with optional + or -)
kk
    pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)$'
    return bool(re.match(pattern, user_input.strip()))

# History list
conversion_history = []

# GUI Application
def convert():
    temp_input = entry_temp.get().strip()
    conversion_type = conversion_var.get()

    if not temp_input:
        messagebox.showerror("Input Error", "Temperature input cannot be empty.")
        return

    if not is_valid_number(temp_input):
        messagebox.showerror("Invalid Input", "Please enter a valid number (e.g., 36.6, -10, +0.5).")
        return

    try:
        temperature = float(temp_input)
    except ValueError:
        messagebox.showerror("Conversion Error", "Could not convert input to a number.")
        return

    if conversion_type == "Celsius to Fahrenheit":
        converted = celsius_to_fahrenheit(temperature)
        result = f"{temperature}°C = {converted:.2f}°F"
    else:
        converted = fahrenheit_to_celsius(temperature)
        result = f"{temperature}°F = {converted:.2f}°C"

    conversion_history.append(result)
    output_label.config(text=result)
    update_history()

def update_history():
    history_listbox.delete(0, tk.END)
    for item in conversion_history[-10:]:  # show last 10 entries
        history_listbox.insert(tk.END, item)

# Create GUI window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x400")
root.resizable(False, False)

# Widgets
entry_label = tk.Label(root, text="Enter Temperature:")
entry_label.pack(pady=5)

entry_temp = tk.Entry(root, width=20)
entry_temp.pack(pady=5)

conversion_var = tk.StringVar(value="Celsius to Fahrenheit")
conversion_dropdown = ttk.Combobox(root, textvariable=conversion_var, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly")
conversion_dropdown.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
output_label.pack(pady=10)

history_label = tk.Label(root, text="Conversion History (Last 10):")
history_label.pack(pady=5)

history_listbox = tk.Listbox(root, width=50, height=10)
history_listbox.pack(pady=5)

# Start GUI loop

if __name__ == "__main__":
    try:
        root.mainloop()
    except Exception as e:
        print("Error starting GUI:", e)

"""

