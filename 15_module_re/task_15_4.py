# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
from pprint import pprint

def get_ints_without_description(config):
    '''
    Функция, которая обрабатывает конфигурацию и возвращает список имен интерфейсов,
    на которых нет описания (команды description).
    '''

    regex = (r'interface (?P<intf>\S+)')

    result_all = []
    result_with_desc = []
    with open(config) as f:
        for line in f:
            match = re.match(regex, line)
            if match:
                result_all.append(match.group('intf'))
                interface = match.group('intf')
            elif line.startswith(' description'):
                result_with_desc.append(interface)
    return [x for x in list(set(result_all)) if x not in result_with_desc]

if __name__ == "__main__":
    pprint(get_ints_without_description('config_r2.txt'))


# import re


# def get_ints_without_description(config):
#     regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
#                        r"(?P<descr> description \S+)?")
#     with open(config) as src:
#         match = regex.finditer(src.read())
#         result = [m.group('intf') for m in match if m.lastgroup == 'intf']
#         return result


# def get_ints_without_description(filename):
#     result_list = []
#     regex = r"^interface (?P<intf>\S+)|^ description (.+)\n"
#     with open(filename) as f:
#         for line in f:
#             match_line = re.search(regex, line)
#             if match_line:
#                 if match_line.lastgroup == "intf":
#                     intf = match_line.group("intf")
#                     result_list.append(intf)
#                 else:
#                     result_list.remove(intf)
#     return result_list



