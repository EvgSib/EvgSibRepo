# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

def convert_ios_nat_to_asa(file_config, file_result):
    '''
    Функция, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
    Функция ожидает на вход 2 файла:
    - имя файла, в котором находится правила NAT Cisco IOS
    - имя файла, в который надо записать полученные правила NAT для ASA
    '''
    with open(file_config) as src, open(file_result, 'w') as dest:
        for line in src:
            regex = r"ip nat inside source static (?P<protocol>\S+) (?P<ip>\S+) (?P<port1>\d+) interface (?P<interface>\S+) (?P<port2>\d+)"
            match = re.search(regex, line)
            ip = match.group('ip')
            protocol = match.group('protocol')
            port1 = match.group('port1')
            port2 = match.group('port2')

            dest.write(f'object network LOCAL_{ip}\n')
            dest.write(f' host {ip}\n')
            dest.write(f' nat (inside,outside) static interface service {protocol} {port1} {port2}\n')

if __name__ == "__main__":
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_nat_ASA.txt')


# import re


# def convert_ios_nat_to_asa(cisco_ios, cisco_asa):
#     regex = (
#         "tcp (?P<local_ip>\S+) +(?P<lport>\d+) +interface +\S+ (?P<outside_port>\d+)"
#     )
#     asa_template = (
#         "object network LOCAL_{local_ip}\n"
#         " host {local_ip}\n"
#         " nat (inside,outside) static interface service tcp {lport} {outside_port}\n"
#     )
#     with open(cisco_ios) as f, open(cisco_asa, "w") as asa_nat_cfg:
#         data = re.finditer(regex, f.read())
#         for match in data:
#             asa_nat_cfg.write(asa_template.format(**match.groupdict()))


# if __name__ == "__main__":
#     convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_config.txt")





