# -*- coding: utf-8 -*-

n = 4
if n < 0:
    print("Факториал не определен для отрицательных чисел.")
elif n == 0:
    print("1")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)
