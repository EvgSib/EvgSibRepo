# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
input_user = input('Enter VLAN number: ')

with open("CAM_table.txt", "r") as f:
    for line in f:
        line_split = line.split()
        if line_split and line_split[0].isdigit() and line_split[0] == input_user:
            vlan, mac, _, intf = line_split
            print(f"{vlan:9}{mac:20}{intf}")


# newlist = []

# with open("CAM_table.txt", "r") as f:
#     for line in f:
#         line_split = line.split()
#         if line_split and line_split[0].isdigit():
#             vlan, mac, _, intf = line_split
#             newlist.append([int(vlan), mac, intf])

# input_user = input('Enter VLAN number: ')

# for line in newlist:
#     if line[0] == int(input_user):
#         print(line)







