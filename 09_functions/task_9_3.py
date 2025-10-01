# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint

def get_int_vlan_map(config_filename):
    '''
    Функция, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
    * словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
    {'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17}
    * словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
    {'FastEthernet0/1': [10, 20],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]}
    '''
    result_access = {}
    result_trunk = {}

    with open(config_filename) as f:
        for line in f:
            line_split = line.split()
            if line_split and 'interface' in line:
                _, interface = line_split
            elif line_split and 'switchport access' in line:
                *rest, vlan = line_split
                result_access[interface] = int(vlan)
            elif line_split and 'switchport trunk allowed' in line:
                *rest, vlan = line_split
                vlans = vlan.split(',')
                vlans = [int(vl) for vl in vlans]
                result_trunk[interface] = vlans
    return result_access, result_trunk

if __name__ == '__main__':
    pprint(get_int_vlan_map("config_sw1.txt"))

# def get_int_vlan_map(config_filename):
#     access_dict = {}
#     trunk_dict = {}

#     with open(config_filename) as cfg:
#         for line in cfg:
#             line = line.rstrip()
#             if line.startswith("interface"):
#                 intf = line.split()[1]
#             elif "access vlan" in line:
#                 access_dict[intf] = int(line.split()[-1])
#             elif "trunk allowed" in line:
#                 trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
#         return access_dict, trunk_dict
