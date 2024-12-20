# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt') as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            print(line.rstrip())

# with open(filename) as f:
#    for line in f:
#        if not line.startswith("!"):
#            value_list = []
#            for value in ignore:
#                if not value in line:
#                    value_list.append('False')
#                else:
#                    value_list.append('True')
#            if 'True' in  value_list:
#                continue
#            else:
#                print(line.rstrip())
