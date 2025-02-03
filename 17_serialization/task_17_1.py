# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
from pprint import pprint
import csv
import glob

def write_dhcp_snooping_to_csv(filenames, output):
    '''
    Функция, которая обрабатывает вывод команды show dhcp snooping binding
    из разных файлов и записывает обработанные данные в csv файл.
    '''
    regex = (r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)')
    result = [['switch', 'mac', 'ip', 'vlan', 'intf']]
    for file in filenames:
        device = file.split('_')[0]
        with open(file) as f:
            for m in re.finditer(regex, f.read()):
                list_file = [device, m.group('mac'), m.group('ip'), m.group('vlan'), m.group('intf')]
                result.append(list_file)

    with open(output, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(result)
    return result

if __name__ == "__main__":
    sh_dhcp_snoop_files = glob.glob('*_dhcp_snooping.txt') #список из 3-х файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt,sw3_dhcp_snooping.txt
    pprint(write_dhcp_snooping_to_csv(sh_dhcp_snoop_files, 'sw_dhcp_snooping.csv'))


def write_dhcp_snooping_to_csv(filenames, output):
    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
        for filename in filenames:
            switch = re.search("([^/]+)_dhcp_snooping.txt", filename).group(1)
            with open(filename) as f:
                for line in f:
                    match = re.search(regex, line)
                    if match:
                        writer.writerow((switch,) + match.groups())


if __name__ == "__main__":
    sh_dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
    print(sh_dhcp_snoop_files)
    write_dhcp_snooping_to_csv(sh_dhcp_snoop_files, "example_csv.csv")






