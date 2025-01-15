# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками ([], []):
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#видео 12 useful modules part 1 с 33.43

import subprocess

def ping_ip_addresses(list_ip):
    print(f'Пингую ip адреса из списка {list_ip}')
    reachable_hosts = []
    unreachable_hosts = []
    for ip in list_ip:
        result = subprocess.run(f'ping {ip} -c 1 -n', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
        if result.returncode == 0:
            reachable_hosts.append(ip)
        else:
            unreachable_hosts.append(ip)
    result_tuple = tuple([reachable_hosts, unreachable_hosts])
    print('в итоговом кортеже')
    print('([список доступных IP-адресов], [список недоступных IP-адресов])')
    return result_tuple

if __name__ == "__main__":
    list_ip = ['127.0.0.1', '192.168.0.1', '8.8.8.8', '192.168.2.1', '192.168.0.11', '192.168.190.11', '192.168.15.1']
    output = ping_ip_addresses(list_ip)
    print(output)

