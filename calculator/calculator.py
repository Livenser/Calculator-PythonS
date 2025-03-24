import tkinter as tk
from tkinter import font as tkFont
from math import sqrt, sin, cos, tan, log, log10, factorial, pi, radians, degrees
import winsound  
from tkinter import messagebox
import matplotlib.pyplot as plt  

dark_mode = True  
degree_mode = True  

def calculate():
    try:
        expression = input_field.get()  
        result = eval(expression)  
        input_field.delete(0, tk.END)  
        input_field.insert(tk.END, str(result))  
        history_list.append(f"{expression} = {result}")  
        update_history()  
    except ZeroDivisionError:  
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Math Error")  
    except Exception as e:  
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Syntax Error")  

def append_to_input(value):
    current = input_field.get()  
    input_field.delete(0, tk.END)  
    input_field.insert(tk.END, current + value)  
    play_click_sound()  

def clear_input():
    input_field.delete(0, tk.END)  
    play_click_sound()  

def backspace():
    current = input_field.get()  
    input_field.delete(0, tk.END)  
    input_field.insert(tk.END, current[:-1])  
    play_click_sound()  

def play_click_sound():
    try:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)  
    except Exception as e:  
        print(f"Error playing sound: {e}")  

def update_history():
    history_text.config(state=tk.NORMAL)  
    history_text.delete(1.0, tk.END)  
    for entry in reversed(history_list[-10:]):  
        history_text.insert(tk.END, entry + "\n")  
    history_text.config(state=tk.DISABLED)  

def toggle_theme():
    global dark_mode  
    dark_mode = not dark_mode  
    if dark_mode:
        BG_COLOR = "#1e1e1e"  
        BUTTON_BG_COLOR = "#2c2c2c"  
        TEXT_COLOR = "#ffffff"  
        theme_button.config(text="☀️ Light Mode")
    else:
        BG_COLOR = "#ffffff"  
        BUTTON_BG_COLOR = "#f0f0f0"  
        TEXT_COLOR = "#000000"  
        theme_button.config(text="🌙 Dark Mode")
    
    root.configure(bg=BG_COLOR)
    input_frame.configure(bg=BG_COLOR)
    input_field.configure(bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
    history_frame.configure(bg=BG_COLOR)
    history_label.configure(bg=BG_COLOR, fg=TEXT_COLOR)
    history_text.configure(bg=BG_COLOR, fg=TEXT_COLOR)
    button_frame.configure(bg=BG_COLOR)
    for widget in button_frame.winfo_children():
        widget.configure(bg=BUTTON_BG_COLOR, fg=TEXT_COLOR)

def toggle_degree_mode():
    global degree_mode  
    degree_mode = not degree_mode  
    if degree_mode:
        degree_button.config(text="Deg")
    else:
        degree_button.config(text="Rad")

def plot_graph():
    try:
        expression = input_field.get()  
        x = [i * 0.1 for i in range(-100, 101)]  
        y = [eval(expression.replace("x", f"({xi})")) for xi in x]  
        plt.figure(figsize=(6, 4))  
        plt.plot(x, y, label=expression)  
        plt.axhline(0, color='black', linewidth=0.5)  
        plt.axvline(0, color='black', linewidth=0.5)  
        plt.grid(color='gray', linestyle='--', linewidth=0.5)  
        plt.legend()  
        plt.title("Graph of " + expression)  
        plt.xlabel("x")  
        plt.ylabel("y")  
        plt.show()  
    except Exception as e:  
        messagebox.showerror("Error", "Invalid expression for graph plotting.")  

root = tk.Tk()
root.title("Calculator Aruvu")
root.geometry("600x800")
root.minsize(500, 700)

BG_COLOR = "#1e1e1e"  
BUTTON_BG_COLOR = "#2c2c2c"  
BUTTON_HOVER_COLOR = "#3c3c3c"  
EQUAL_BUTTON_COLOR = "#33cc33"  
CLEAR_BUTTON_COLOR = "#ff4d4d"  
INPUT_FIELD_COLOR = "#2c2c2c"  
TEXT_COLOR = "#ffffff"  

root.configure(bg=BG_COLOR)

input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(fill=tk.X, padx=20, pady=(20, 10))

input_field = tk.Entry(input_frame, font=("Helvetica", 24, "bold"), justify=tk.RIGHT, bd=0, relief=tk.FLAT, bg=INPUT_FIELD_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
input_field.pack(fill=tk.X, padx=10, pady=10)

history_frame = tk.Frame(root, bg=BG_COLOR)
history_frame.pack(fill=tk.X, padx=20, pady=(10, 0))

history_label = tk.Label(history_frame, text="History:", font=("Helvetica", 14, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
history_label.pack(anchor=tk.W)

history_text = tk.Text(history_frame, height=5, font=("Helvetica", 12), bg=INPUT_FIELD_COLOR, fg=TEXT_COLOR, bd=0, relief=tk.FLAT, state=tk.DISABLED)
history_text.pack(fill=tk.X, padx=10, pady=(5, 10))

history_list = []

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('C', 3, 0), ('0', 3, 1), ('.', 3, 2), ('+', 3, 3),
    ('sqrt', 4, 0), ('=', 4, 1), ('Back', 4, 2), ('Clear', 4, 3),
]

def on_enter(e):
    if e.widget.cget("text") == "=":
        e.widget['bg'] = "#28a745"
    elif e.widget.cget("text") == "C":
        e.widget['bg'] = "#dc3545"
    else:
        e.widget['bg'] = BUTTON_HOVER_COLOR

def on_leave(e):
    if e.widget.cget("text") == "=":
        e.widget['bg'] = EQUAL_BUTTON_COLOR
    elif e.widget.cget("text") == "C":
        e.widget['bg'] = CLEAR_BUTTON_COLOR
    else:
        e.widget['bg'] = BUTTON_BG_COLOR

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(button_frame, text=text, bg=EQUAL_BUTTON_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=calculate, bd=0, relief=tk.FLAT, activebackground="#28a745")
    elif text == 'C':
        btn = tk.Button(button_frame, text=text, bg=CLEAR_BUTTON_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=clear_input, bd=0, relief=tk.FLAT, activebackground="#dc3545")
    elif text == 'Back':
        btn = tk.Button(button_frame, text=text, bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=backspace, bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)
    elif text == 'Clear':
        btn = tk.Button(button_frame, text=text, bg=CLEAR_BUTTON_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=lambda: input_field.delete(0, tk.END), bd=0, relief=tk.FLAT, activebackground="#dc3545")
    elif text == 'sqrt':
        btn = tk.Button(button_frame, text=text, bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=lambda: append_to_input("sqrt("), bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)
    else:
        btn = tk.Button(button_frame, text=text, bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 18, "bold"), command=lambda t=text: append_to_input(t), bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)

    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)
    btn.bind("<Enter>", on_enter)  
    btn.bind("<Leave>", on_leave)  

theme_button = tk.Button(button_frame, text="☀️ Light Mode", bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 14, "bold"), command=toggle_theme, bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)
theme_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

degree_button = tk.Button(button_frame, text="Deg", bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 14, "bold"), command=toggle_degree_mode, bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)
degree_button.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

graph_button = tk.Button(button_frame, text="Plot Graph", bg=BUTTON_BG_COLOR, fg="white", font=("Helvetica", 14, "bold"), command=plot_graph, bd=0, relief=tk.FLAT, activebackground=BUTTON_HOVER_COLOR)
graph_button.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

for i in range(7):  
    button_frame.rowconfigure(i, weight=1)
for i in range(4):  
    button_frame.columnconfigure(i, weight=1)

root.mainloop()