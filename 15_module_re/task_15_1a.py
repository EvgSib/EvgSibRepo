# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
from pprint import pprint

def get_ip_from_cfg(config):
    with open(config) as f:
        regex = re.compile(
            r"interface (?P<intf>\S+)\n"
            r"( .*\n)*"
            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
        )
        match = regex.finditer(f.read())

    result = {m.group("intf"): m.group("ip", "mask") for m in match}
    return result

pprint(get_ip_from_cfg('config_r111.txt'))



# def get_ip_from_cfg(config):
#     regex = (r'interface (?P<intf>\S+)'
#     r'|ip address (?P<ip>\S+) (?P<mask>\S+)')

#     result = {}
#     with open(config) as f:
#         for line in f:
#             match = re.search(regex, line)
#             if match:
#                 if match.lastgroup == 'intf':
#                     interface = match.group('intf')
#                 else:
#                     result[interface] = match.group('ip', 'mask')
#     return result


# pprint(get_ip_from_cfg('config_r2.txt'))
