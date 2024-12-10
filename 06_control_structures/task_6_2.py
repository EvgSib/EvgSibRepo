# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
input_user = input('введите IP-адрес в формате 10.0.1.1: ')
ip_user = int(input_user.split('.')[0])

if 1 <= ip_user <= 223:
    print('unicast')
elif 224 <= ip_user <= 239:
    print('multicast')
elif input_user == '255.255.255.255':
    print('local broadcast')
elif input_user == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
