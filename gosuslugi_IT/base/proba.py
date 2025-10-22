# -*- coding: utf-8 -*-
'''
Пример 1 (тест):
Входные данные:
MCMXCIV

Выходные данные:
1994

Пример 2 (тест):
Входные данные:
XLII

Выходные данные:
42

Пример 3 (тест):
Входные данные:
CDXLIV

Выходные данные:
444

Пример 4 (тест):
Входные данные:
MMXX

Выходные данные:
2020

Пример 5 (тест):
Входные данные:
DCCCXLV

Выходные данные:
845

Пример 6 (тест):
Входные данные:
CCLXXXI

Выходные данные:
281

Пример 7 (из задания):
Входные данные:
MCMXXCIV

Выходные данные:
1984

Выходные данные:
0,1,2

Пример 8 (из задания):
Входные данные:
MCCXXXIV

Выходные данные:
1234

если левое значение больше правого, то это окончательное число
если левое значение меньше правого, то из правого нужно вычесть левое значение
'''


def roman_to_decimal(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    out, mx = 0, 0
    for cur in map(lambda c: roman_numerals[c], roman_numeral[::-1]):
# без переворота roman_numeral = '1000  100 1000 10   100    1    5  '
#                roman_numeral = ' V     I   C    X    M     C    M  '
#                roman_numeral = ' 5     1  100  10  1000   100  1000'
        if cur >= mx:
            out = out + cur
            mx = cur
        else:
            out = out - cur
    return out

roman_number = 'MCMXCIV'
decimal_number = roman_to_decimal(roman_number)
print(decimal_number)





