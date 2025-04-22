import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator - Light Mode")
        self.geometry("600x600")
        self.history = []
        self.theme = 'light'

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.style = ttk.Style(self)
        self.set_theme(self.theme)

        main_frame = ttk.Frame(self)
        main_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.entry = ttk.Entry(main_frame, font=("Arial", 20))
        self.entry.pack(fill='x', pady=(0, 10))

        self.basic_frame = ttk.LabelFrame(main_frame, text="Basic Operations")
        self.basic_frame.pack(fill='x', pady=5)

        self.scientific_frame = ttk.LabelFrame(main_frame, text="Scientific Functions")
        self.scientific_frame.pack(fill='x', pady=5)

        self.control_frame = ttk.Frame(main_frame)
        self.control_frame.pack(fill='x', pady=5)

        self.create_basic_buttons()
        self.create_scientific_buttons()

        ttk.Button(self.control_frame, text="Toggle Theme", command=self.toggle_theme).pack(side='left', padx=5)

        # History Side Panel
        self.history_frame = ttk.LabelFrame(self, text="History")
        self.history_frame.pack(side='right', fill='y', padx=5, pady=10)

        self.history_listbox = tk.Listbox(self.history_frame, height=25, font=("Courier", 10))
        self.history_listbox.pack(side='top', fill='both', expand=True)

    def create_basic_buttons(self):
        rows = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('(', ')', 'C', 'DEL')
        ]
        for row in rows:
            frame = ttk.Frame(self.basic_frame)
            frame.pack(expand=True, fill='x')
            for btn in row:
                ttk.Button(frame, text=btn, command=lambda b=btn: self.on_button_click(b)).pack(side='left', expand=True, fill='both')

    def create_scientific_buttons(self):
        functions = [
            ('sqrt', 'x^y', 'log₁₀', 'ln'),
            ('sin', 'cos', 'tan', 'fact')
        ]
        for row in functions:
            frame = ttk.Frame(self.scientific_frame)
            frame.pack(expand=True, fill='x')
            for btn in row:
                display_text = btn.replace('x^y', '^').replace('log₁₀', 'log').replace('fact', '!')
                ttk.Button(frame, text=btn, command=lambda b=display_text: self.on_button_click(b)).pack(side='left', expand=True, fill='both')

    def bind_keys(self):
        self.bind('<Return>', lambda event: self.on_button_click('='))
        self.bind('<BackSpace>', lambda event: self.on_button_click('DEL'))
        for char in '0123456789+-*/().':
            self.bind(char, lambda event, c=char: self.on_button_click(c))

    def toggle_theme(self):
        self.theme = 'dark' if self.theme == 'light' else 'light'
        self.set_theme(self.theme)
        self.title(f"Scientific Calculator - {'Dark' if self.theme == 'dark' else 'Light'} Mode")

    def set_theme(self, theme):
        if theme == 'dark':
            self.configure(bg='#2e2e2e')
            self.style.configure('.', background='#2e2e2e', foreground='white', fieldbackground='#3e3e3e')
            self.style.map('TButton', background=[('active', '#505050')])
        else:
            self.configure(bg='SystemButtonFace')
            self.style.configure('.', background='SystemButtonFace', foreground='black', fieldbackground='white')

    def update_history(self, expression, result):
        display = f"{expression} = {result}"
        self.history.append(display)
        if len(self.history) > 10:
            self.history.pop(0)
        self.history_listbox.delete(0, 'end')
        for item in self.history:
            self.history_listbox.insert('end', item)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, 'end')
        elif char == '=':
            try:
                expression = self.entry.get()
                expression_eval = expression.replace('^', '**')
                expression_eval = expression_eval.replace('sqrt', 'math.sqrt')
                expression_eval = expression_eval.replace('log', 'math.log10')
                expression_eval = expression_eval.replace('ln', 'math.log')
                expression_eval = expression_eval.replace('sin', 'math.sin')
                expression_eval = expression_eval.replace('cos', 'math.cos')
                expression_eval = expression_eval.replace('tan', 'math.tan')
                expression_eval = expression_eval.replace('!', 'math.factorial')
                result = eval(expression_eval, {"math": math, "__builtins__": {}})
                result_str = str(result)
                self.entry.delete(0, 'end')
                self.entry.insert('end', result_str)
                self.update_history(expression, result_str)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'DEL':
            current = self.entry.get()
            self.entry.delete(0, 'end')
            self.entry.insert('end', current[:-1])
        else:
            self.entry.insert('end', char)

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
