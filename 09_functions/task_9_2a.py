# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

from pprint import pprint

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    {"FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает словарь, в котором:
    - ключ это наименование интерфейса
    - значение это конфигкрация порта в режиме trunk на основе шаблона
    """
    result = {}
    for intf, vlans in intf_vlan_mapping.items():
        command_intf = f"interface {intf}"
        list_trunk = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ",".join([str(vl) for vl in vlans])
                command_trunk_vlan = f"{command} {vlans_str}"
                list_trunk.append(command_trunk_vlan)
            else:
                command_trunk = f"{command}"
                list_trunk.append(command_trunk)
        result[command_intf] = list_trunk
    return result

pprint(generate_trunk_config(trunk_config, trunk_mode_template))




