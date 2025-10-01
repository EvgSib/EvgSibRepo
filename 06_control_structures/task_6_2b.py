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
    ip_address = input("Введите IP-адрес в формате XXX.XXX.XXX.XXX: ")
    octets = ip_address.split(".")
    correct_ip = True

    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                correct_ip = False
                break
    else:
        correct_ip = False
    if correct_ip:
        break
    print("Неправильный IP-адрес")

if correct_ip:
    ip_user = int(octets[0])
    if ip_user in range(1, 224):
        print('unicast')
    elif 224 <= ip_user <= 239:
        print('multicast')
    elif ip_address == '255.255.255.255':
        print('local broadcast')
    elif ip_address == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')

