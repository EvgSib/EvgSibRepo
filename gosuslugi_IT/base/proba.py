# -*- coding: utf-8 -*-
'''
Пример 3 (тест):
Входные данные:
2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12

Выходные данные:
Q1:
- Кольцо: 7
- Шляпа: 4
Q2:
- Браслет: 18
'''

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


def generate_quarterly_report(data):
    items_by_quarter = {}
    # Анализ входных данных и группировка элементов по кварталам
    for item_str in data.split(';'):
        date, product, quantity = item_str.split(':')
        item = Item(date, product, quantity)
        quarter = item.quarter
        if quarter not in items_by_quarter:
            items_by_quarter[quarter] = {}
        if product in items_by_quarter[quarter]:
            items_by_quarter[quarter][product] += int(quantity)
        else:
            items_by_quarter[quarter][product] = int(quantity)

    for key, value in sorted(items_by_quarter.items()):
        yield f"{key}:"
        for x, y in sorted(value.items()):
            yield f"- {x}: {y}"

# def property(func):
#     def wrapper(self):  # Важно: обёртка должна принимать `self`
#         func(self)  # Вызов оригинального метода, передавая `self`
#     return wrapper

input_data = '2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12'
quarterly_report_generator = generate_quarterly_report(input_data)
for report in quarterly_report_generator:
    print(report)
'''
Выходные данные:
Q1:
- Кольцо: 7
- Шляпа: 4
Q2:
- Браслет: 18
'''


# from config import SETTINGS; SETTINGS = {'debug': False}
# from config import SETTINGS as cfg; cfg['debug'] = False
# import config; config.SETTINGS['debug'] = False
# import config; config.SETTINGS.debug = False
# import config; config.SETTINGS = {'debug': False}
# print(config.SETTINGS['debug'])

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Что-то происходит до вызова функции")
#         Вызов оригинальной функции со всеми аргументами
#         res = func(*args, **kwargs)
#         print("Что-то происходит после вызова функции")
#         return res
#     return wrapper

# @my_decorator это тоже самое, что func = my_decorator(func)
# @my_decorator
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(f"Результат: {result}")

# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит до вызова функции")
#         func()  # Вызов оригинальной функции
#         print("Что-то происходит после вызова функции")
#     return wrapper

# @my_decorator это тоже самое, что func = my_decorator(func)
# @my_decorator
# def say_hello():
#     print("Привет, мир!")

# say_hello()
# say_hello()
# say_hello()


# на вход функции property подается функция quarter и возвращается тоже функция quarter
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

# date = '2023-03-20'
# f = property(quarter)
# f()

# def countdown(n):
#     def inner():
#         nonlocal n
#         print(n)
#         n = n-1
#     return inner

# f = countdown(5)
# f()
# f()
# f()


# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит до вызова функции")
#         func()  # Вызов оригинальной функции
#         print("Что-то происходит после вызова функции")
#     return wrapper

# def my_decorator():
#     print('вызвана функция my_decorator')
#     def wrapper():
#         print("вызвана функция wrapper")
#         a = 10
#         b = 15
#         return f'выводим сумму {a+b}'
#     return wrapper

# f = my_decorator()
# print(f())

# Декорирование функции вручную
# decorated_hello = my_decorator(say_hello)
# Вызов декорированной функции
# decorated_hello()
# @my_decorator
# def say_hello():
#     print("Привет, мир!")

# Вызов декорированной функции
# say_hello()

