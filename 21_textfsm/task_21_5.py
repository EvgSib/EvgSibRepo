# -*- coding: utf-8 -*-
"""
Задание 21.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в
параллельных потоках функцию send_and_parse_show_command из задания 21.4.

Параметры функции send_and_parse_command_parallel:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* templates_path - путь к каталогу с шаблонами TextFSM
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать словарь:
* ключи - IP-адрес устройства с которого получен вывод
* значения - список словарей (вывод который возвращает функция send_and_parse_show_command)

Пример словаря:
{'192.168.100.1': [{'address': '192.168.100.1',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '192.168.200.1',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.2': [{'address': '192.168.100.2',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '10.100.23.2',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}]}

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
from task_21_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import os
import yaml

def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    '''
    Функция запускает в параллельных потоках функцию send_and_parse_show_command из задания 21.4
    Параметры функции send_and_parse_command_parallel:
        * devices - список словарей с параметрами подключения к устройствам
        * command - команда
        * templates_path - путь к каталогу с шаблонами TextFSM
        * limit - максимальное количество параллельных потоков (по умолчанию 3)
    '''

    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_list = []
        for device in devices:
            future = executor.submit(send_and_parse_show_command, device, command, templates_path)
            future_list.append(future)
        output = {}
        for device, f in zip(devices, future_list):
            output[device["host"]] = f.result()
    return output

if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    path_dir = f"{os.getcwd()}/templates"
    pprint(send_and_parse_command_parallel(devices, command, path_dir))

# ниже решение Н.Самойленко, в нем циклы объединены в list comprehensions и dict comprehensions

# def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
#     '''
#     Функция запускает в параллельных потоках функцию send_and_parse_show_command из задания 21.4
#     Параметры функции send_and_parse_command_parallel:
#         * devices - список словарей с параметрами подключения к устройствам
#         * command - команда
#         * templates_path - путь к каталогу с шаблонами TextFSM
#         * limit - максимальное количество параллельных потоков (по умолчанию 3)
#     '''

#     with ThreadPoolExecutor(max_workers=limit) as executor:
#         results = executor.map(send_and_parse_show_command, devices, repeat(command))
#         dict_result = {}
#         for output in results:
#             dict_result[output[0]['address']] = output
#         print("### Все потоки отработали")
#         return dict_result
