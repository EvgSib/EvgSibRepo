# -*- coding: utf-8 -*-
'''
Анализ текста
Описание:
В рамках работы над проектом по анализу текста на натуральном языке требуется
реализовать функцию, возвращающую манхэттенское расстояние между строками.
Оно вычисляется следующим образом:
Общее расстояние равно сумме расстояний между буквами
Расстояние между двумя буквами равно модулю разности их мест в алфавите
Расстояние между буквой и любым другим символом (или отсутствием символа,
если одна строка короче другой) равно её месту в алфавите.

Формат ввода:
Две произвольных строки (от 3 до 250 символов, латинские буквы, пробелы и знаки препинания)

Формат вывода:
Строка, содержащая число, являющееся вычисленным вышеописанным образом манхэттенским расстоянием

Пример 1 (тест):
Входные данные:
data science
data science

Выходные данные:
0

Пример 2 (тест):
Входные данные:
data analysis
data

Выходные данные:
100

Пример 3 (тест):
Входные данные:
machine learning
machine learning

Выходные данные:
0

Пример 4 (тест):
Входные данные:
deep learning
learning

Выходные данные:
108

Пример 5 (тест):
Входные данные:
For whom the bell tolls?
For you

Выходные данные:
170

Пример 5 (из задания):
Входные данные:
For you
For whom the bell tolls?

Выходные данные:
170

Пример 6 (из задания):
Входные данные:
Something
Something

Выходные данные:
0
Расстояние между буквой и любым другим символом (или отсутствием символа,
если одна строка короче другой) равно её месту в алфавите.
'''

def manhattan_distance(string_one: str, string_two: str) -> str:
    if len(string_one) > len(string_two):
        rest_str = string_one[len(string_two):]
        string_one = string_one[:len(string_two)]
    elif len(string_one) < len(string_two):
        rest_str = string_two[len(string_one):]
        string_two = string_two[:len(string_one)]
    else:
        rest_str = []

    sum_rest_str = []
    for i in rest_str:
        if i.isalpha():
            sum_rest_str.append(ord(i) - ord('a') + 1)

    sum_rest_str = sum(sum_rest_str)
    for char1, char2 in zip(string_one, string_two):
        if char1.isalpha() and char2.isalpha():
            sum_rest_str += abs(ord(char1) - ord(char2))
        elif not char1.isalpha() and char2.isalpha():
            sum_rest_str += abs(ord(char2) - ord('a') + 1)
        elif not char2.isalpha() and char1.isalpha():
            sum_rest_str += abs(ord(char1) - ord('a') + 1)
    return str(sum_rest_str)

string_one = input()
string_two = input()
distance = manhattan_distance(string_one,string_two)
print(distance)

