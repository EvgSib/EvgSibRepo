# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""

from netmiko import ConnectHandler
from pprint import pprint
from textfsm import clitable
import os
import yaml

def send_and_parse_show_command(device_dict, command, templates_path, index = "index"):
    with ConnectHandler(**device_dict) as r1:
        r1.enable()
        command_output = r1.send_command(command)
#     инициализируем класс, передав ему имя файла index, в котором хранится соответствие
#     между шаблонами и командами, и указываем имя каталога templates_path, в котором хранятся шаблоны
    cli_table = clitable.CliTable(index, templates_path)
#     методу ParseCmd надо передать вывод команды и словарь с параметрами
    attributes_dict = {'Command': command, 'Vendor': 'cisco_ios'}
    cli_table.ParseCmd(command_output, attributes_dict)

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)
    list_result = [dict(zip(header,list_in_list)) for list_in_list in data_rows]

    return list_result


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(dev, "sh ip int br", templates_path=full_pth)
        pprint(result, width=120)

# ниже решение Н.Самойленко(более правильное), т.к. функция send_and_parse_show_command
# импортирует функцию parse_command_dynamic из задания 21_3, а я ее запихал в send_and_parse_show_command

# from task_21_3 import parse_command_dynamic
# import os
# from pprint import pprint
# from netmiko import ConnectHandler
# import yaml

# def send_and_parse_show_command(device_dict, command, templates_path, index="index"):
#     attributes = {"Command": command, "Vendor": device_dict["device_type"]}
#     with ConnectHandler(**device_dict) as ssh:
#         ssh.enable()
#         output = ssh.send_command(command)
#         parsed_data = parse_command_dynamic(
#             output, attributes, templ_path=templates_path, index_file=index
#         )
#     return parsed_data


# if __name__ == "__main__":
#     full_pth = os.path.join(os.getcwd(), "templates")
#     with open("devices.yaml") as f:
#         devices = yaml.safe_load(f)
#     for dev in devices:
#         result = send_and_parse_show_command(
#             dev, "sh ip int br", templates_path=full_pth
#         )
#         pprint(result, width=120)
