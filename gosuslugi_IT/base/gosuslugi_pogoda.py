# -*- coding: utf-8 -*-
'''
Вы работаете в команде веб-платформы с прогнозом погоды. Вы работаете над модулем,
который будет выдавать статистическую информацию о температуре за определенный период.
На вход подается список из целых чисел. Ваша задача — определить, сколько чисел в этом
списке являются положительными, сколько отрицательными и сколько из них равны нулю.
Вам нужно вывести не сами числа, а их количество в каждой категории.

Входные данные:
5 -2 0 0 7 8 -1
Выходные данные:
выше нуля: 3, ниже нуля: 2, равна нулю: 2
'''


def process(input_string: str) -> str:
    in_list = input_string.split(' ')
    list_more0 = []
    list_0 = []
    list_less0 = []
    for i in in_list:
        if int(i) > 0:
            list_more0.append(i)
        elif int(i) == 0:
            list_0.append(i)
        else:
            list_less0.append(i)
    return f'выше нуля: {len(list_more0)}, ниже нуля: {len(list_0)}, равна нулю: {len(list_less0)}'

input_string = input()
output_string = process(input_string)
print(output_string)
