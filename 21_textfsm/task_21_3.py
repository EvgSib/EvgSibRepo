# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""

from pprint import pprint
from textfsm import clitable

def parse_command_dynamic(command_output, attributes_dict, index_file = "index", templ_path = "templates"):
    # инициализируем класс, передав ему имя файла index_file, в котором хранится соответствие
    # между шаблонами и командами, и указываем имя каталога templ_path, в котором хранятся шаблоны
    cli_table = clitable.CliTable(index_file, templ_path)
    # методу ParseCmd надо передать вывод команды и словарь с параметрами
    cli_table.ParseCmd(command_output, attributes_dict)

    data_rows = [list(row) for row in cli_table]
    header = list(cli_table.header)
    list_result = [dict(zip(header,list_in_list)) for list_in_list in data_rows]
    return list_result


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    attributes_dict = {'Command': 'sh ip int br', 'Vendor': 'cisco_ios'}
    result = parse_command_dynamic(output, attributes_dict)
    pprint(result, width=100)



