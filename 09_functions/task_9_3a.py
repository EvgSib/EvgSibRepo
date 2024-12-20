# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint

def get_int_vlan_map(config_filename):

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
            elif line_split and 'duplex auto' in line:
                if interface in result_access or interface in result_trunk:
                    continue
                else:
                    result_access[interface] = 1
    return result_access, result_trunk

pprint(get_int_vlan_map("config_sw2.txt"))


# def get_int_vlan_map(config_filename):
#     access_port_dict = {}
#     trunk_port_dict = {}
#     with open(config_filename) as f:
#         for line in f:
#             if line.startswith("interface FastEthernet"):
#                 current_interface = line.split()[-1]
#                Сразу указываем, что интерфейсу
#                соответствует 1 влан в access_port_dict
#                 access_port_dict[current_interface] = 1
#             elif "switchport access vlan" in line:
#                если нашлось другое значение VLAN,
#                оно перепишет предыдущее соответствие
#                 access_port_dict[current_interface] = int(line.split()[-1])
#             elif "switchport trunk allowed vlan" in line:
#                 vlans = [int(i) for i in line.split()[-1].split(",")]
#                 trunk_port_dict[current_interface] = vlans
#                если встретилась команда trunk allowed vlan
#                надо удалить интерфейс из словаря access_port_dict
#                 del access_port_dict[current_interface]
#     return access_port_dict, trunk_port_dict
