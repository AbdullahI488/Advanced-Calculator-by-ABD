import tkinter as tk

calculation = ""

# define all the functions that will be used
def calculator_sqrt():
    global calculation
    calculation += "√"
    update_display()

def calculator_add(symbol):
    global calculation
    calculation += str(symbol)
    update_display()

def calculator_eval():
    global calculation
    try:
        calculation = calculation.replace("√", "**0.5")
        calculation = str(eval(calculation))
        update_display()
    except Exception as A:
        clear_field()
        text_result.insert(tk.END, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

def update_display():
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, calculation)

root = tk.Tk()
root.title("Advance Calculator by ABD")
root.geometry("720x480")

# make the grid

for row in range(6):
    tk.Grid.rowconfigure(root, row, weight=1)
for col in range(4):
    tk.Grid.columnconfigure(root, col, weight=1)

text_result = tk.Text(root, height=4,bg="skyblue", width=27, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=4, sticky="nsew")

button_labels = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "0", "(", ")", "/",
    "sqrt", "**", "Clear", "="
]

# use for loop to add the button function and writing to the button

row_num = 1
col_num = 0
for label in button_labels:
    but = tk.Button(root, text=label, width=10, font=("Arial", 24),bg='lightblue', command=lambda button_label=label: button_click(button_label))
    but.grid(row=row_num, column=col_num, sticky="nsew")
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# checks and sees if button is clear, equal or sqrt if yes does the thingy if not then adds the thingy to the writey
def button_click(label):
    if label == "sqrt":
        calculator_sqrt()
    elif label == "Clear":
        clear_field()
    elif label == "=":
        calculator_eval()
    else:
        calculator_add(label)

root.mainloop()

# The code isnt all too safe however works amazingly has everything you would need from a cal tbh, the end.
