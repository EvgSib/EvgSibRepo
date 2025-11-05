# -*- coding: utf-8 -*-
'''
Экстремумы
Описание:
Вы разрабатываете инструмент, который помогает анализировать колебания показателей — например,
температуру в течение дня, уровень шума или изменения на графике акций.
Иногда нужно быстро понять, где были всплески или провалы — то есть такие значения,
которые заметно выше или ниже окружающих.
Ваша задача — найти экстремумы: точки, которые строго больше или строго меньше n соседних значений слева и справа от него.
Если у числа нет нужного числа соседей слева и справа — оно не считается экстремумом.

Формат ввода:
Число n соседних значений и строка, содержащая разделённые запятыми вещественные числа (0 ≤ x ≤ 10).

Формат вывода:
Строка формата (без кавычек): <тип экстремума>: <значение экстремума>,
<тип экстремума>: <значение экстремума>, ... ИЛИ «Экстремумов не обнаружено.»

Пример 1:
Входные данные:
2
0.891,0.987,0.995,0.969,0.7,0.128
Выходные данные:
max: 0.995

Пример 2:
Входные данные:
1
0.73727,2.96021,3.45525,4.6169,7.17337,9.91429,2.2754,5.85553,0.938094,8.21642
Выходные данные:
max: 9.91429, min: 0.938094

Пример 3:
Входные данные:
1
0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9
Выходные данные:
Экстремумов не обнаружено

Пример 4(тест):
Входные данные:
1
9.0,8.0,7.0,6.0,7.0,4.0,3.0,2.0,1.0
Выходные данные:
min: 6.0,max: 7.0

Пример 5(тест):
Входные данные:
1
0.0,1.0,0.0,1.0,0.0,1.0,0.0
Выходные данные:
max: 1.0,min: 0.0,max: 1.0,min: 0.0,max: 1.0

Пример 6(тест):
Входные данные:
1
5.0,5.0,5.0,5.0,5.0
Выходные данные:
Экстремумов не обнаружено

Пример 7(тест):
Входные данные:
2
10.0,9.0,8.0,7.0,6.0,5.0
Выходные данные:
Экстремумов не обнаружено
'''

def extreme_values(data: str, number_of_neighbors: int) -> str:
    number_of_neighbors = int(number_of_neighbors)
    data = data.split(',')
    result = []
    for item in range(1,len(data)):
        if item < number_of_neighbors or item > (len(data) - 1 - number_of_neighbors):
            continue
        else:
            true_list_max = []
            true_list_min = []
            for i in range(item - number_of_neighbors, item + number_of_neighbors + 1):
                if i == item:
                    continue
                elif data[item] > data[i]:
                    true_list_max.append(True)
                    true_list_min.append(False)
                elif data[item] < data[i]:
                    true_list_max.append(False)
                    true_list_min.append(True)
                else:
                    true_list_max.append(False)
                    true_list_min.append(False)
            if all(true_list_max):
                result.append(f'max: {data[item]}')
            elif all(true_list_min):
                result.append(f'min: {data[item]}')

    result_max_min = ', '.join(result)
    if result_max_min:
        return result_max_min
    else:
        return "Экстремумов не обнаружено"

number_of_neighbors = input()
data = input()
extremes = extreme_values(data, number_of_neighbors)
print(extremes)
