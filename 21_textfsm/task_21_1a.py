# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
Вывод должен быть таким:
[{'intf': 'FastEthernet0/0', 'address': '192.168.100.1', 'status': 'up', 'protocol': 'up'},
{'intf': 'FastEthernet0/1', 'address': 'unassigned', 'status': 'administratively down', 'protocol': 'down'}]
"""

from pprint import pprint
from netmiko import ConnectHandler
import textfsm

# мой вариант
def parse_output_to_dict(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)

        list_result = [dict(zip(header,list_in_list)) for list_in_list in result]

    return list_result

if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    pprint(result, width=120)

# def parse_output_to_dict(template, command_output):
#     with open(template) as tmpl:
#         fsm = textfsm.TextFSM(tmpl)
#         result = fsm.ParseTextToDicts(command_output)
#     return result

# мой вариант (словарь в другом виде)
# def parse_output_to_dict(template, command_output):
#     with open(template) as tmpl:
#         parser = textfsm.TextFSM(tmpl)
#         header = parser.header
#         result = parser.ParseText(command_output)

#         list_result = []
#         for i in range(len(result[0])):
#             middle_dict = {}
#             list_value = [list_in_list[i] for list_in_list in result]
#             middle_dict[header[i]] = list_value
#             list_result.append(middle_dict)

#     return list_result
