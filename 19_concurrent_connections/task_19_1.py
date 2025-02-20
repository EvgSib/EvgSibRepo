# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import time
import logging
from tabulate import tabulate
import ipaddress
import csv

logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(format = '%(threadName)s %(name)s %(levelname)s: %(message)s', level=logging.INFO)

def ping_ip_address(ip):
    '''
    Функция, которая проверяет пингуются ли IP-адрес.
    На вход функции подается IP-адрес.
    Функция возвращает True или False.
    '''
    print(f'Пингую ip адрес {ip}')
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    logging.info(start_msg.format(datetime.now().time(), ip))
    result = subprocess.run(f'ping {ip} -c 2 -n', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
    logging.info(received_msg.format(datetime.now().time(), ip))
    if result.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, limit=3):
    '''
    Функция, которая запускает функцию ping_ip_address в параллельных потоках.
    На вход функции подается:
      * ip_list - список IP-адресов
      * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Функция возвращает кортеж с двумя списками:
    ([список доступных IP-адресов], [список недоступных IP-адресов])
    '''
    with ThreadPoolExecutor(max_workers=limit) as executor:
        list_map = []
        result = executor.map(ping_ip_address, ip_list)
        for ip, output in zip(ip_list, result):
            tuple_ip = (ip, output)
            list_map.append(tuple_ip)
        reachable_hosts = []
        unreachable_hosts = []
        for item in list_map:
            if item[1]:
                reachable_hosts.append(item[0])
            else:
                unreachable_hosts.append(item[0])
        result_tuple = tuple([reachable_hosts, unreachable_hosts])
    return result_tuple


def convert_ranges_to_ip_list(in_list):
    '''
    Функция, которая конвертирует список IP-адресов в разных форматах в список,
    где каждый IP-адрес указан отдельно. Этот список нужно передать на вход функции ping_ip_addresses.

    Функция возвращает список IP-адресов, в котором каждый IP-адрес указан отдельно.
    '''
    ip_list = []
    for ip_address in in_list:
        if "-" in ip_address:
            start_ip, stop_ip = ip_address.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                ip_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_list.append(ip_address)
    return ip_list


if __name__ == "__main__":
    in_list = input(
'''Введите список IP-адресов, которые нужно пропинговать.
Пример ввода:
10.1.1.1, 10.1.1.1-10.1.1.10, 192.168.1.1-10
''')
    output = [n.strip() for n in in_list.split(',')]
    ip_list = convert_ranges_to_ip_list(output)
    result_tuple = ping_ip_addresses(ip_list, limit=27)
    dict_for_tabulate = {'Reachable': result_tuple[0], 'Unreachable': result_tuple[1]}
    # эта часть кода для красивого вывода на stdout с заголовками tabulate
    output = tabulate(dict_for_tabulate, headers="keys")
    print(output)
    # эта часть кода для записи вывода в CSV файл
    filename = 'csv_ping_ip.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f, dialect='excel')
        key_list = list(dict_for_tabulate.keys())
        limit_reach = len(dict_for_tabulate['Reachable'])
        limit_unreach = len(dict_for_tabulate['Unreachable'])
        if limit_reach>limit_unreach:
            difference = limit_reach - limit_unreach
            lists = ['' for _ in range(difference)]
            dict_for_tabulate['Unreachable'].extend(lists)
        else:
            difference = limit_unreach - limit_reach
            lists = ['' for _ in range(difference)]
            dict_for_tabulate['Reachable'].extend(lists)
        writer.writerow(dict_for_tabulate.keys())
        limit = len(dict_for_tabulate['Unreachable'])
        for i in range(limit):
            writer.writerow([dict_for_tabulate[x][i] for x in key_list])
        print(f'Результаты сохранены в файл {filename}')



