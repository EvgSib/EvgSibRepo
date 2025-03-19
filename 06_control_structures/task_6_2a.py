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

ip_address = input("Enter ip address: ")
octets = ip_address.split(".")
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        # тут второе условие int(octet) in range(256)
        # проверяется только в том случае, если первое условие истина
        # Если встретился хоть один октет с нарушением,
        # дальше можно не смотреть
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Неправильный IP-адрес")
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1, 224):
        print("unicast")
    elif octets_num[0] in range(224, 240):
        print("multicast")
    elif ip_address == "255.255.255.255":
        print("local broadcast")
    elif ip_address == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")




# input_user = input('введите IP-адрес в формате XXX.XXX.XXX.XXX: ')
# ip_split = input_user.split('.')

# for number in ip_split:
#     check_ip = number.isdigit() and input_user.split()[0].count('.') == 3 and len(ip_split) == 4

# if check_ip:
#     ip_user = int(ip_split[0])
#     if ip_user in range(0, 224):
#         print('unicast')
#     elif 224 <= ip_user <= 239:
#         print('multicast')
#     elif input_user == '255.255.255.255':
#         print('local broadcast')
#     elif input_user == '0.0.0.0':
#         print('unassigned')
#     else:
#         print('unused')
# else:
#     print('Неправильный IP-адрес')

