# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    input_user = input('введите IP-адрес в формате XXX.XXX.XXX.XXX: ')
    ip_split = input_user.split('.')

    for number in ip_split:
        check_ip = number.isdigit() and input_user.split()[0].count('.') == 3 and len(ip_split) == 4
    if check_ip:
        break
    print('Неправильный IP-адрес')

if check_ip:
    ip_user = int(ip_split[0])
    if ip_user in range(0, 224):
        print('unicast')
    elif 224 <= ip_user <= 239:
        print('multicast')
    elif input_user == '255.255.255.255':
        print('local broadcast')
    elif input_user == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')

