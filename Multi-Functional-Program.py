import tkinter as tk
import random
import string
from datetime import datetime
from tkinter import messagebox

# Создаем основное окно
root = tk.Tk()
root.title("Мультифункциональная программа")

# Функция для программы "1-100"
def random_number():
    number = random.randint(1, 100)
    messagebox.showinfo("Случайное число", f"Число: {number}")

# Функция для Калькулятора
def calculate():
    try:
        result = eval(calc_entry.get())
        calc_result_label.config(text=f"Результат: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка в вычислении: {e}")

# Функция для Генератора паролей
def generate_password():
    length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Сгенерированный пароль", f"Пароль: {password}")

# Функция для отображения текущего времени
def show_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messagebox.showinfo("Текущее время", f"Время: {current_time}")

# Кнопка для программы "1-100"
btn_random_number = tk.Button(root, text="Случайное число (1-100)", command=random_number)
btn_random_number.pack(pady=10)

# Калькулятор
calc_label = tk.Label(root, text="Калькулятор")
calc_label.pack()
calc_entry = tk.Entry(root)
calc_entry.pack()
calc_button = tk.Button(root, text="Вычислить", command=calculate)
calc_button.pack()
calc_result_label = tk.Label(root, text="Результат: ")
calc_result_label.pack()

# Кнопка для Генератора паролей
btn_password_generator = tk.Button(root, text="Генератор пароля", command=generate_password)
btn_password_generator.pack(pady=10)

# Кнопка для отображения текущего времени
btn_show_time = tk.Button(root, text="Показать время", command=show_time)
btn_show_time.pack(pady=10)

# Запуск основного цикла приложения
root.mainloop()
