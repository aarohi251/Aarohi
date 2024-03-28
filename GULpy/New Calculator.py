import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    
    if button_value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_value)

root = tk.Tk()
root.title("Colorful Calculator")

# Entry widget for displaying the input and result
entry = tk.Entry(root, width=20, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button creation function
def create_button(row, col, text, bg_color, command=lambda: on_click(text)):
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg=bg_color, command=command)
    button.grid(row=row, column=col)

# Define button layout
buttons = [
    ('7', '#7FB3D5'), ('8', '#7FB3D5'), ('9', '#7FB3D5'), ('/', '#FF8C00'),
    ('4', '#7FB3D5'), ('5', '#7FB3D5'), ('6', '#7FB3D5'), ('*', '#FF8C00'),
    ('1', '#7FB3D5'), ('2', '#7FB3D5'), ('3', '#7FB3D5'), ('-', '#FF8C00'),
    ('0', '#7FB3D5'), ('.', '#7FB3D5'), ('C', '#FF6961'), ('+', '#FF8C00'),
    ('=', '#90EE90')
]

# Create buttons
for i, (text, color) in enumerate(buttons):
    row_val = i // 4 + 1
    col_val = i % 4
    create_button(row_val, col_val, text, color)

root.mainloop()
