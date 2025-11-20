# -*- coding: utf-8 -*-

# for i in range(10):
#     for j in range(i):
#         pass
# result = i
# print(result)

# d= [1,2,3]
# result = dict(zip(d, enumerate(d))).values()
# print(result)
# res = dict([(e[1], e) for e in enumerate(d)]).values()
# print(res)


# class A:
#     i = 10
#     def f():
#         i +=1
# A.i = 100
# a = A
# a.i = 1000
# A.f()
# print(A.i)

# m = [[1,2,3], [4,5,6], [7,8,9]]
# r = [m[j][i] for i in range(len(m[0])) for j in range(len(m)) if i > j]
# r = [row[j] for row in [m[i] for i in range(len(m))] for j in range(len(m)) if i<j]
# r = [m[i][j] for i in range(len(m)) for j in range(len(m)) if i >j]
# r = [m[i][i+j] for i in range(len(m)) for j in range(len(m)-i)]
# print(r)


# def f(a,b):
#     if b == 0:
#         return a
#     else:
#         return f(a + 1, b - 1)
# def g(a,b):
#     if b == 0:
#         return a
#     else:
#         return f(a, g(a, b - 1))
# x = g(6,4)


# print(x)

# def f(s):
#     return s + s
# print(f(f('ab')))

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Деление на ноль!")
# finally:
#     print("Завершение")

# i: int = 1e111+111
# results = [False, False, False]
# results[0] = i == 1e111+111
# results[1] = i == float(i)
# results[2] = i == int(float(i))
# print(results)


# class C:
#     def __init__(self):
#         def g():
#             yield 1
#             yield 2
#             yield 3
#         g = g
# c = C()
# print(next(C.g()), end = ' ')
# print(next(C.g()))


# s = [1, 2, 3, 4, 5]
# print([n if n>= m else 0 for n,m in zip([s[i] for i in range(len(s) -1, -1,-1)],s)])

# try:
#     int('abc')
# except ValueError as e:
#     print(type(e))

# def f(n):
#     if n > 0:
#         yield f(n-1)
#     else:
#         yield 0
# result = list(f(2))

# print(result)

# r = range(3,0,-1)
# for i in range(0,4):
#     print(all(r), end = ' ')


# flag = False
# for i in range(0, 6):
#     if i == 3:
#         continue
#         flag = True
#         print(i)
#     if flag:
#         print(i)
#         break
#     print(i)

# def area(radius):
#     return 3.14*radius*radius
# def area(side):
#     return side*side
# def area(width, height):
#     return width*height
# result = area(1)

# dictionary = {1: 1, 3: 4, 5: 7, 7:10, 9:13}
# e = enumerate(dictionary)
# d = []
# for i in e:
#     d.append(sum(i))
# print(d)



# def f(a,b):
#     if b == 0:
#         return a
#     else:
#         return f(a + 1, b - 1)
# def g(a,b):
#     if b == 0:
#         return 0
#     else:
#         return f(a, g(a, b - 1))
# x = g(6,4)
# print(x)

