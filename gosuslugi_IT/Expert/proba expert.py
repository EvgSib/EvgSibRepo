# -*- coding: utf-8 -*-
class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)


    @property
    def quarter(self):
        month = int(self.date.split('-')[1])
        if 1 <= month <= 3:
            return "Q1"
        elif 4 <= month <= 6:
            return "Q2"
        elif 7 <= month <= 9:
            return "Q3"
        else:
            return "Q4"

    def property(func):
        def wrapper():
            print("Что-то происходит до вызова функции")
            func()  # Вызов оригинальной функции
            print("Что-то происходит после вызова функции")
        return wrapper

item = Item('2023-02-05', 'Шляпа', '4')
print(item.date)

# def property(func):
#     def wrapper(*args):
#         print("Что-то происходит до вызова функции")
#         result = func(*args)  # Вызов оригинальной функции
#         print(result)
#         print("Что-то происходит после вызова функции")
#         return result
#     return wrapper

# @property
# def quarter(date):
#     month = int(date.split('-')[1])
#     if 1 <= month <= 3:
#         return "Q1"
#     elif 4 <= month <= 6:
#         return "Q2"
#     elif 7 <= month <= 9:
#         return "Q3"
#     else:
#         return "Q4"

# Вызов декорированной функции
# quarter('2023-04-20')

# Определяем декоратор
def log_method_call(func):
    """Декоратор для логирования вызовов методов."""
    # Внутренняя функция-обёртка принимает все аргументы, включая 'self'
    def wrapper(self, *args, **kwargs):
        print(f"Вызов метода '{func.__name__}' с аргументами: {args}, {kwargs}")
        result = func(self, *args, **kwargs) # Вызов исходного метода
        print(f"Метод '{func.__name__}' завершён. Результат: {result}")
        return result
    return wrapper

# Определяем класс и применяем декоратор к методу
class Calculator:
    def __init__(self, value):
        self.value = value

    @log_method_call
    def add(self, other):
        """Метод для сложения чисел."""
        self.value += other
        return self.value

# Создаём экземпляр класса и вызываем декорированный метод
calc = Calculator(10)
result = calc.add(5)

print(f"Итоговое значение: {result}")






















