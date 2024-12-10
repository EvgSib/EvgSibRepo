# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

input_user = input('введите IP-адрес в формате XXX.XXX.XXX.XXX: ')
ip_split = input_user.split('.')

for number in ip_split:
    check_ip = number.isdigit() and input_user.split()[0].count('.') == 3 and len(ip_split) == 4

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
else:
    print('Неправильный IP-адрес')


