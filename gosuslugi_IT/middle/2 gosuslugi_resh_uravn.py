# -*- coding: utf-8 -*-
'''
Решение уравнений
(БЫЛО. Проходит тесты на госуслугах)
Описание:
Вы разрабатываете компонент веб-приложения для онлайн-репетиторов и образовательных платформ.
В системе предусмотрено автоматическое решение заданий по математике.
Чтобы упростить проверку и анализ заданий, нужно реализовать функцию,
которая будет автоматически решать простейшие линейные уравнения, введённые пользователем.

Формат ввода:
Строка, содержащая линейное уравнение, состоящая из вещественных чисел, знаков '+', '-', '*',
произвольного числа копий символа, являющегося переменной, и одного знака '='.
Строка гарантированно является корректным линейным уравнением.

Формат вывода:
Строка формата (без кавычек):
<переменная> = <ответ>,
ответ является вещественным числом, округлённым до ближайших тысячных.

Пример 1:
Входные данные:
3x + 5 = 10x - 5
Выходные данные:
x = 1.429

Пример 2:
Входные данные:
3.14159 + z - 10z = 181 - 0.15z
Выходные данные:
z = -20.097

Пример 3:
Входные данные:
-3x + 5 = 7x - 5
Выходные данные:
n = 1.0

Пример 4:
Входные данные:
-3x * 5 = 5x - 5
Выходные данные:
n = 1.0
'''

def solve_linear_equation(equation: str) -> str:
    list_eq = equation.split('=')
    list_eq = [i.replace(' ', '') for i in list_eq] #убираем все пробелы в каждой строке
    list_split = []
    for num in list_eq:
        indices = [position for position, element in enumerate(num) if element in "+-*"]
        list_spl = [num[start:end] for start, end in zip([0] + indices, indices + [None])]
        list_spl = [i for i in list_spl if i] #удаляем пустые строки из списка
        list_split.append(list_spl)
    list_spl_left, list_spl_right = list_split[0], list_split[1]
    list_var = []
    list_num = []
    for item_l in list_spl_left:
        if any(char.isalpha() for char in item_l):
            name_var = item_l[-1]
            list_var.append(item_l)
        else:
            list_num.append(float(item_l) * -1)
    for item_r in list_spl_right:
        if any(char.isalpha() for char in item_r):
            list_var.append(str(float(item_r[:-1])* -1)+item_r[-1])
        else:
            list_num.append(float(item_r))

    list_var = [i[:-1] for i in list_var]
    list_var_fin = []
    for m in list_var:
        if m in '+-*':
            list_var_fin.append(float(m + '1'))
        elif m == '':
            list_var_fin.append(1)
        else:
            list_var_fin.append(float(m))
    result = round(sum(list_num) / sum(list_var_fin), 3)
#     return list_var, list_num
    return name_var + ' = ' + str(result)

equation = input()
solution = solve_linear_equation(equation)
print(solution)




# def solve_linear_equation(equation: str) -> str:
#     list_eq = equation.split('=')
#     list_eq = [i.replace(' ', '') for i in list_eq] #убираем все пробелы в каждой строке
#     list_split = []
#     for num in list_eq:
#         indices = [position for position, element in enumerate(num) if element in "+-*"]
#         list_spl = [num[start:end] for start, end in zip([0] + indices, indices + [None])]
#         list_spl = [i for i in list_spl if i] #удаляем пустые строки из списка
#         list_split.append(list_spl)
#     list_spl_left, list_spl_right = list_split[0], list_split[1]
#     list_var = []
#     list_num = []
#     for item_l in list_spl_left:
#         if any(char.isalpha() for char in item_l):
#             if item_l[0] in '*':
#                 pass
#             else:
#                 name_var = item_l[-1]
#                 list_var.append(item_l)
#         else:
#             if item_l[0] in '*':
#                 pass
#             else:
#                 list_num.append(float(item_l) * -1)
#     for item_r in list_spl_right:
#         if any(char.isalpha() for char in item_r):
#             if item_r[0] in '*':
#                 pass
#             else:
#                 list_var.append(str(float(item_r[:-1])* -1)+item_r[-1])
#         else:
#             if item_r[0] in '*':
#                 pass
#             else:
#                 list_num.append(float(item_r))
#     list_var = [i[:-1] for i in list_var]
#     list_var_fin = []
#     for m in list_var:
#         if m in '+-*':
#             list_var_fin.append(float(m + '1'))
#         elif m == '':
#             list_var_fin.append(1)
#         else:
#             list_var_fin.append(float(m))
#     result = round(sum(list_num) / sum(list_var_fin), 3)
#     return name_var + ' = ' + str(result)

# equation = input()
# solution = solve_linear_equation(equation)
# print(solution)




#     left_eq, right_eq = list_eq[0], list_eq[1]
#     indices_left = [position for position, element in enumerate(left_eq) if element in "+-*"]
#     list_spl_left = [left_eq[start:end] for start, end in zip([0] + indices_left, indices_left + [None])]
#     list_spl_left = [i for i in list_spl_left if i] #удаляем пустые строки из списка
#     indices_right = [position for position, element in enumerate(right_eq) if element in "+-*"]
#     list_spl_right = [right_eq[start:end] for start, end in zip([0] + indices_right, indices_right + [None])]
#     list_spl_right = [i for i in list_spl_right if i] #удаляем пустые строки из списка
