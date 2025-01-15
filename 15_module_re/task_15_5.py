# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""

import re
from pprint import pprint

def generate_description_from_cdp(config):
    with open(config) as f:
        regex = re.compile(r'(?P<device_id>\S+)\s+(?P<local_intf>\w+ \S+)\s+\d+\s+(\w\s){3}\s+\d+\s+(?P<port_id>\w+ \S+)')
        match = regex.finditer(f.read())

    result = {m.group("local_intf"): f'description Connected to {m.group("device_id")} port {m.group("port_id")}' for m in match}
    return result

pprint(generate_description_from_cdp('sh_cdp_n_sw1.txt'))


