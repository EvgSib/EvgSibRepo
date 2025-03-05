# -*- coding: utf-8 -*-
"""
Задание 21.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding
и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 21.1.
"""

from pprint import pprint
from task_21_1 import parse_command_output

if __name__ == "__main__":
    with open("output/sh_ip_dhcp_snooping.txt") as show:
        output = show.read()
    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
    pprint(result)

'''
Содержимое файла sh_ip_int_br.template:
Value mac ((?:\S+:){5}\S+)
Value ip ((?:\d+.){3}\d+)
Value vlan (\d+)
Value intf (\S+)

Start
  ^${mac}\s+${ip}\s+\d+\s+\S+\s+${vlan}\s+${intf} -> Record
'''
# просто так функция из 21_1 не работает, сначала нужно открыть и считать файл sh_ip_dhcp_snooping.txt
# или использовать функцию ниже
# def parse_command_output(template, command_output):
#     with open(template) as f, open(command_output) as output:
#         parser = textfsm.TextFSM(f)
#         header = parser.header
#         result = parser.ParseText(output.read())
#     return [header] + result
