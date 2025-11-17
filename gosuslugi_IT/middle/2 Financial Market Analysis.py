# -*- coding: utf-8 -*-
'''
Анализ финансовых рынков
Описание:
Вы разрабатываете программу для анализа финансовых рынков. Вам предоставлен временной ряд цен акций определенной компании.
Вы хотите найти дни, когда цена акции оставалась выше всех последующих цен в течение периода,
то есть ваша задача – выявить все доминирующие элементы среди цен на акции. Элемент массива является доминирующим,
если он строго больше, чем все элементы справа от него, в том числе – если это последний элемент в массиве.

Формат ввода:
Одна строка, в которой чередуются целые числа, разделенные пробелами. Длина списка – не больше 100 элементов.

Формат вывода:
Одна строка, в которой чередуются целые числа, разделенные пробелами.
В строке содержатся только числа, соответствующие определению «доминирующий элемент массива».

Пример 1:
Входные данные:
1 2 1 4 7 5

Выходные данные:
7 5

Пример 2:
Входные данные:
7 6 5 4 3 1 2

Выходные данные:
7 6 5 4 3 2
'''

def get_dominate_prices(stock_prices: str) -> str:
    stock_prices = stock_prices.split()
    result = []
    for i in range(0, len(stock_prices)):
        if i == len(stock_prices) - 1:
            result.append(stock_prices[i])
        true_false = []
        for j in range(i+1, len(stock_prices)):
            if int(stock_prices[i]) > int(stock_prices[j]):
               true_false.append(True)
            else:
                true_false.append(False)
                break
        if all(true_false) and not true_false == []:
            result.append(stock_prices[i])
    return ' '.join(result)

stock_prices = input()
dominate_prices = get_dominate_prices(stock_prices)
print(dominate_prices)





