# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#чтобы файл запустился из терминала нужно скпировать
#файл со скриптом и config_sw1.txt в site-packages и запустить
#python@debian: $ python task_7_2b.py config_sw1.txt config_sw1_output.txt

from sys import argv
filename1 = argv[1]
filename2 = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(filename1) as src, open(filename2, 'w') as dest:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            dest.write(line)
