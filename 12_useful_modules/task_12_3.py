# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

# from tabulate import tabulate

# def print_ip_table(reach_ip, unreach_ip):
#     table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
#     print(tabulate(table, headers="keys"))

# if __name__ == "__main__":
#     reach_ip = ["10.1.1.1", "10.1.1.2"]
#     unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
#     print_ip_table(reach_ip, unreach_ip)


# ниже скрипт, который получает список, конвертирует его в список ip-адресов по заданию 12_2 пингует адреса
# и возвращает успешно пропингованные и нет ip-адреса
# Это довольно лучше, чем вышеуказанныя функция

from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list
from tabulate import tabulate

def print_ip_table(in_list):
    list_convert_ranges = convert_ranges_to_ip_list(in_list)
    in_list_print_ip_table = ping_ip_addresses(list_convert_ranges)
    dict_for_tabulate = {'Reachable': in_list_print_ip_table[0], 'Unreachable': in_list_print_ip_table[1]}
    output = tabulate(dict_for_tabulate, headers="keys")
    return output

if __name__ == '__main__':
    in_list = ['8.8.4.4', '1.1.1.1-2', '172.21.41.128-172.21.41.129']
    print(print_ip_table(in_list))


