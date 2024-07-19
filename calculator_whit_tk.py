import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        print('You can not divide number to 0.')
    else:
        return number1 / number2

def calculator():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = combo.get()

        if operation == '+':
            result = add(num1, num2)

        elif operation == '-':
            result = subtract(num1, num2)

        if operation == '*':
            result = multiply(num1, num2)

        if operation == '/':
            result = divide(num1, num2)

        messagebox.showinfo('result', f'result= {result}')
    except ValueError:
        messagebox.showinfo('Enter the correct form.')


#making the window
root = tk.Tk()
root.title('Calculator')
root.geometry('500x300')

leable1 = tk.Label(root, text='First number: ')
leable1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

leable2 = tk.Label(root, text='Secound number: ')
leable2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

combo = ttk.Combobox(root, values=['+', '-', '*', '/'])
combo.pack(pady=5)
combo.current(0)

botton = tk.Button(root, text='Calculat', command=calculator)
botton.pack(pady=20)

root.mainloop()
