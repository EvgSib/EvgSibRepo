# -*- coding: utf-8 -*-
'''
Интерпретатор
Описание:
Вы работаете над интерпретатором некоторого языка. Требуется реализовать функционал
оценки выражений при объявленных функциях. В синтаксисе этого языка вызов функции записывается как
(<идентификатор функции>, <аргумент 1>, <аргумент 2>,… <аргумент n>).
Синтаксис объявления функций, следующий:
Тело может содержать целочисленные константы, имена аргументов и знаки “+”, “-“, “*”, “%”.
Аргументы и имена функций состоят из строчных букв английского алфавита. Аргументы – целые числа.

Формат ввода
Две строки:
Первая строка содержит объявление функции, в формате
(define (<имя функции> <аргумент 1> <аргумент 2> ...) (<тело>))
Вторая строка содержит выражение, подвергающееся интерпретации,
в котором используется вышеобъявленная функция.
Строки гарантированно корректны.

Формат вывода
Строка, содержащая результат интерпретации выражения.

Пример 1 (из задания)
Входные данные:
(define (add x y) (x + y))
(add 2 3)

Выходные данные:
5

Пример 2 (из задания)
Входные данные:
(define (subtract a b) (a - b))
(subtract 5 2)

Выходные данные:
3


Пример 3 (тест):
Входные данные:
(define (square x) (x * x))
(square 6)

Выходные данные:
36

Пример 4 (тест):
Входные данные:
(define (cube x) (x * x * x))
(cube 3)

Выходные данные:
27

Пример 5 (тест):
Входные данные:
(define (modulus x y) (x % y))
(modulus 10 3)

Выходные данные:
1

Пример 6 (тест):
Входные данные:
(define (increment x) (x + 1))
(increment 7)

Выходные данные:
8

Пример 7 (из задания):
Входные данные:
(define (decrement x) (x - 1))
(decrement 10)

Выходные данные:
9
'''

import re

class Interpreter:
    def __init__(self, definition: str):
        "Ваш код"
        regex = r'\(define \((?P<func_args>.+)\) \((?P<function>.+)\)\)'
        match = re.search(regex, definition)
        d = match.groupdict() #{'func_args': 'add x y', 'function': 'x + y'}
        self.name_func = d['func_args'].split()[0]  # 'add'
        self.args = d['func_args'].split()[1:]  # ['x', 'y']
        self.function = d['function']  # 'x + y'

    def evaluate(self, expression: str) -> str:
        "Ваш код"
        match = re.search(r'\((?P<f>\S+) (?P<args>.+)\)', expression)
        d2 = match.groupdict() #{'f': 'add', 'args': '2 3'}
        if self.name_func == d2['f']:
            dict_arg = dict(zip(self.args, d2['args'].split())) #{'x': '2', 'y': '3'}
            lst_func = self.function.split() #['x', '+', 'y']
            res = []
            for item in lst_func:
                if item in dict_arg:
                    res.append(dict_arg[item])
                else:
                    res.append(item)
            return eval(''.join(res))

definition = input()
my_interpreter = Interpreter(definition) #в задании инициализация класса указана с маленькой буквы
expression = input()
evaluation = my_interpreter.evaluate(expression)
print(evaluation)

