"""
Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

"""
from pprint import pprint

ignore = ["duplex", "alias", "configuration"]

def ignore_command(command, ignore):
    '''
    True, если в команде содержится слово из списка ignore
    '''
    ignore_status = False
    words = command.split()
    for word in ignore:
        if word in words:
            ignore_status = True
    return ignore_status

# result = {}
# with open('config_sw1_1.txt') as f:
#     for line in f:
#         if not line.startswith("!") and not ignore_command(line, ignore) and line != '\n':
#             if not line.startswith(' '):
#                 list_value = []
#                 result[line.rstrip()] = list_value
#             if line.startswith(' '):
#                 list_value.append(line.rstrip())

# pprint(result)


config_dict = {}
with open('config_sw1.txt') as f:
    for line in f:
        line = line.rstrip()
        if line and not (line.startswith("!") or ignore_command(line, ignore)):
            if line[0].isalnum():
                section = line
                config_dict[section] = []
            else:
                config_dict[section].append(line.strip())
pprint(config_dict)






