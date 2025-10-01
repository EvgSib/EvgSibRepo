# -*- coding: utf-8 -*-
'''
БЫЛО
Описание:
Вы разрабатываете программу для учета продаж в интернет-магазине.
На вход программе подается список цен товаров. Вам необходимо определить,
какие товары стоят дороже средней цены всех товаров из списка –
на такие товары впоследствии применяется скидка. Если таких товаров нет, выведите «Нет».

Формат ввода:
Одна строка, содержащая список целых или дробных чисел (цен товаров),
разделенных запятой. Числа находятся в диапазоне 0<x<1000000.

Формат вывода:
Цены, которые превышают среднюю цену по всем товарам из списка,
с сохранением исходного порядка. Цены, равные средней, НЕ выводятся.
Каждая цена должна быть выведена на новой строке. Если таких цен нет, выводится «Нет».

Пример 1:
Входные данные:
10,20,30,40,50

Выходные данные:
40
50

Пример 2:
Входные данные:
5,5,5,5

Выходные данные:
Нет

Пример 3:
Входные данные:
10.5,20,15.75,30,25.5

Выходные данные:
30
25.5

'''

def find_expensive_items(prices_string):
    in_list = prices_string.split(',')
    in_list = [float(item) for item in in_list]

    middle_price = sum(in_list) / len(in_list)
    price_list = [price for price in in_list if price > middle_price]

    result = []
    for char in price_list:
        if '.0' in str(char):
           ch_spl = str(char).split('.')
           result.append(ch_spl[0])
        else:
            result.append(char)

    if len(result) != 0:
        return result
    else:
        return 'Нет'
prices_string = input()
result = find_expensive_items(prices_string)
if isinstance(result, list):
    for i in result:
        print(i)
else:
    print(result)

# def find_expensive_items(prices_string):
#     in_list = prices_string.split(',')
#     in_list = [int(item) for item in in_list]
#     price_list = []
#     middle_price = sum(in_list) / len(in_list)
#     for price in in_list:
#         if price > middle_price:
#             price_list.append(price)
#     if len(price_list) != 0:
#         return [i for i in price_list]
#     else:
#         return'нет'
# prices_string = input()
# result = find_expensive_items(prices_string)
# print(result)








