# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
• список с названиями полей
• список кортежей со значениями
Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.
Например, если функции передать как аргументы список headers и список
[("R1", "12.4(24)T1", "Cisco 3825"),
("R2", "15.2(2)T1", "Cisco 2911")]
Функция должна вернуть такой список со словарями:
[{"hostname": "R1", "ios": "12.4(24)T1", "platform": "Cisco 3825"},
{"hostname": "R2", "ios": "15.2(2)T1", "platform": "Cisco 2911"}]
Функция не должна быть привязана к конкретным данным или количеству заголов-
ков/данных в кортежах.
Проверить работу функции:
• первый аргумент - список headers
• второй аргумент - список data
Ограничение: Все задания надо выполнять используя только пройденные темы

"""

from pprint import pprint

headers = ["hostname", "ios", "platform", "ip"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L", "192.268.222.222")
]

def convert_to_dict(headers, sh_list):
    return [dict(zip(headers, i)) for i in sh_list]


pprint(convert_to_dict(headers, data))

# def convert_to_dict(headers, data):
#     length = len(data)
#     output = [dict(zip(headers,data[number])) for number in range(0, length)]
#     return output

# if __name__ == "__main__":
#     headers = ["hostname", "ios", "platform", "ip"]
#     data = [("R1", "12.4(24)T1", "Cisco 3825"),
#     ("R2", "15.2(2)T1", "Cisco 2911"),
#     ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L", "192.168.1.1"),
#     ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L", "10.65.88.88")
#     ]
#     pprint(convert_to_dict(headers, data))
