# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

import ipaddress

# def convert_ranges_to_ip_list(in_list):
#     out_list = []
#     for ip in in_list:
#         if ip.count('.') == 6 and '-' in ip:
#             split_str = ip.split('-')
#             ip1, ip2 = ip.split('-')
#             ip1_ipaddress = ipaddress.IPv4Address(ip1)
#             ip2_ipaddress = ipaddress.IPv4Address(ip2)
#             list2 = [str(ipaddress.ip_address(ip)) for ip in range(int(ip1_ipaddress), int(ip2_ipaddress+1))]
#             for value in list2:
#                 out_list.append(value)
#         elif ip.count('.') == 3 and '-' in ip:
#             split_str = ip.split('-')
#             split_str0 = '.'.join(split_str[0].split('.')[:3])+'.'
#             ip1, ip2 = [split_str[0], split_str0+split_str[1]]
#             ip1_ipaddress = ipaddress.IPv4Address(ip1)
#             ip2_ipaddress = ipaddress.IPv4Address(ip2)
#             list3 = [str(ipaddress.ip_address(ip)) for ip in range(int(ip1_ipaddress), int(ip2_ipaddress+1))]
#             for value in list3:
#                 out_list.append(value)
#         else:
#             out_list.append(ip)
#     return out_list

def convert_ranges_to_ip_list(in_list):
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


if __name__ == '__main__':
    in_list = ['8.8.4.4', '1.1.1.1-4', '172.21.41.128-172.21.41.133']
    print(convert_ranges_to_ip_list(in_list))


