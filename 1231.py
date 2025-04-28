import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    if expression:
        try:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(0, 'Деление на 0')
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, 'Ошибка ввода')

def create_number_buttons():
    numbers = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('0', 4, 0)
    ]
    for (text, row, col) in numbers:
        btn = tk.Button(root, text=text, padx=20, pady=20,
                        font=('Arial', 18),
                        command=lambda num=text: button_click(num))
        btn.grid(row=row, column=col)

def create_operation_buttons():
    operations = [
        ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
    ]
    for (text, row, col) in operations:
        btn = tk.Button(root, text=text, padx=20, pady=20,
                        font=('Arial', 18),
                        command=lambda op=text: button_click(op))
        btn.grid(row=row, column=col)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x500")

display = tk.Entry(root, width=16, font=('Arial', 24),
                   borderwidth=2, relief="groove")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

create_number_buttons()
create_operation_buttons()

btn_equal = tk.Button(root, text='=', padx=20, pady=20,
                      font=('Arial', 18), command=button_equal)
btn_equal.grid(row=4, column=2)

btn_clear = tk.Button(root, text='C', padx=20, pady=20,
                      font=('Arial', 18), command=button_clear)
btn_clear.grid(row=4, column=1)

root.mainloop()
