# -*- coding: utf-8 -*-
'''
Отчёт о продажах за квартал
(прошли все тесты на госуслугах)
Описание:
Вы работаете над модулем для CRM-системы, который помогает менеджерам по продажам готовить автоматизированные отчеты.
Данные о продажах поступают в формате «Дата:Продукт:Количество;Дата:Продукт:Количество;...».
Напишите программу, которая принимает информацию о продажах по датам и возвращает отчет о продажах за каждый квартал.

Формат ввода:
Одна строка с данными в формате «Дата:Продукт:Количество;Дата:Продукт:Количество;...»‎.
Дата в формате YYYY-MM-DD, через двоеточие указано название продукта на русском языке и
через ещё одно двоеточие — целое число, указывающее на количество проданных товаров.
Данные по каждому продукту разделены точкой с запятой.

Формат вывода:
Набор строк, в котором выводится информация о продажах товаров.
Сначала даётся номер квартала с двоеточием, а после — маркированный список с дефисом с названием товара
и с количеством продаж через двоеточие. Кварталы идут по порядку, а товары внутри квартала сортируются по алфавиту.

Пример 1 (из задания):
Входные данные:
2023-01-15:Книга:10;2023-04-20:Флешка:5;2023-07-05:Наушники:8

Выходные данные:
Q1:
- Книга: 10
Q2:
- Флешка: 5
Q3:
- Наушники: 8

Пример 2 (из задания):
Входные данные:
2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12

Выходные данные:
Q1:
- Кольцо: 7
- Шляпа: 4
Q2:
- Браслет: 18

Пример 3 (тест):
Входные данные:
2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12

Выходные данные:
Q1:
- Кольцо: 7
- Шляпа: 4
Q2:
- Браслет: 18

Пример 4 (тест):
Входные данные:
2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8;2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8

Выходные данные:
Q1:
 - Коврик: 12
Q2:
- Бинокль: 20
- Компас: 16

Пример 5 (тест):
Входные данные:
2023-05-20:Шапка:7;2023-02-25:Краска:5;2023-05-05:Мяч:8

Выходные данные:
Q1:
- Краска: 5
Q2:
- Мяч: 8
- Шапка: 7
'''

# обертка для прохождения тестов не нужна, но может это влияет на внутр тесты
def property(func):
    def wrapper(self):  # Важно: обёртка должна принимать `self`
        result = func(self)  # Вызов оригинального метода, передавая `self`
        return result
    return wrapper

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
        i = Item(date, product, quantity)
        quarter = i.quarter() # если без обертки, то тут должно быть quarter = i.quarter и удалить def property
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



input_data = '2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8;2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8'
quarterly_report_generator = generate_quarterly_report(input_data)
for report in quarterly_report_generator:
    print(report)


# ниже приведен код с функцией декоратором, она не обязательна тут

# def property(func):
#     def wrapper(self):  # Важно: обёртка должна принимать `self`
#         result = func(self)  # Вызов оригинального метода, передавая `self`
#         return result
#     return wrapper

# class Item:
#     def __init__(self, date, product, quantity):
#         self.date = date
#         self.product = product
#         self.quantity = int(quantity)


#     @property
#     def quarter(self):
#         month = int(self.date.split('-')[1])
#         if 1 <= month <= 3:
#             return 'Q1'
#         elif 4 <= month <= 6:
#             return 'Q2'
#         elif 7 <= month <= 9:
#             return 'Q3'
#         else:
#             return 'Q4'


# def generate_quarterly_report(data):
#     items_by_quarter = {}
#     Анализ входных данных и группировка элементов по кварталам
#     for item_str in data.split(';'):
#         date, product, quantity = item_str.split(':')
#         item = Item(date, product, quantity)
#         quarter = item.quarter()
#         if quarter not in items_by_quarter:
#             items_by_quarter[quarter] = {}
#         if product in items_by_quarter[quarter]:
#             items_by_quarter[quarter][product] += int(quantity)
#         else:
#             items_by_quarter[quarter][product] = int(quantity)

#     for key, value in sorted(items_by_quarter.items()):
#         yield f"{key}:"
#         for x, y in sorted(value.items()):
#             yield f"- {x}: {y}"


# input_data = input()
# quarterly_report_generator = generate_quarterly_report(input_data)
# for report in quarterly_report_generator:
#     print(report)
