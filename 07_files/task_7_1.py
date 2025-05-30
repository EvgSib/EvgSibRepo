# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = '''
Prefix              {}
AD/Metric           {:<16}
Next-Hop            {:<16}
Last update         {:<16}
Outbound Interface  {:<16}
'''
import re
with open('ospf.txt') as f:
    for line in f:
        line = re.sub(r'([,\[\]])', ' ', line)
        line = line.split()
        print(template.format(line[1], line[2], line[4], line[5], line[6]))



