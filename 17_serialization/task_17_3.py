# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re
from pprint import pprint

def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(r"(?P<r_dev>\w+) +(?P<l_intf>\S+ \S+) +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)")
    connect_dict = {}
    l_dev = re.search(r"(\S+)[>#]", command_output).group(1)
    connect_dict[l_dev] = {}
    for match in regex.finditer(command_output):
        r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
    return connect_dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))


# def parse_sh_cdp_neighbors(command_output):
#     """
#     Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
#     Функция должна вернуть такой словарь:
#     {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
#             'Fa 0/2': {'R6': 'Fa 0/0'}}}
#     """
#     regex = (r'(?P<hostname>\S+)>show cdp neighbors'
#              r'|(?P<Device_ID>\S+) +(?P<Local_Intrfce>\S+ \d*/\d*) .+ (?P<Port_ID>\S+ \d*/\d*)')
#     result = {}
#     dictList = []
#     for line in command_output.split("\n"):
#         line = line.strip()
#         match = re.search(regex, line)
#         if match:
#             if match.lastgroup == 'hostname':
#                 hostname = match.group(match.lastgroup)
#             elif match.lastgroup == 'Port_ID':
#                 _, device_id, local_intrfce, port_id =  match.groups()
#                 dictList.append({local_intrfce: {device_id: port_id}})
#     newDict = {k:v for element in dictList for k,v in element.items()}
#     result[hostname] = newDict
#     return result


# if __name__ == "__main__":
#     with open("sh_cdp_n_r1.txt") as f:
#         pprint(parse_sh_cdp_neighbors(f.read()))


