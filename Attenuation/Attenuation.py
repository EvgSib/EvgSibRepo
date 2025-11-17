# -*- coding: utf-8 -*-
"""
Создать программу, которая на вход ожидает файл с выгрузками команд по уровню оптических сигналов.
В файле "signal_levels_NSK.txt" информация только по оборудованию В.

Функция должна вернуть файл в формате csv со столбцами
Оборудование А,         Оборудование В,        Оборудование B.   Оборудование B.
Уровни сигналов:        Уровни сигналов:       Порт              Наименование
Уровень излучения/      Уровень излучения/
Уровни приема           Уровни приема
-1.3dBm/-2.4dBm         -1.8dBm/-1.9dBm        Twe1/0/1         an02.sbc.Nsk

Уровень приема оборудования А равен уровень излучения оборудования В минус 0.6dBm (затухание на патчкорде):
-1.8dBm - 0.6dBm = -2.4dBm
Уровень излучения оборудования А равен уровень приема оборудования В плюс 0.6dBm (затухание на патчкорде):
-1.9dBm + 0.6dBm = -1.3dBm
"""

import glob
import re
import csv

def signal_levels(data):
    '''
    Функция, которая на вход ожидает файл с выгрузками команд по уровню оптических сигналов.
    На выходе выдает список списков вида:
    [['hostname', 'interface', 'Tx_Power_B/Rx_Power_B', 'Tx_Power_A/Rx_Power_A'], [] ...]
    '''
    pattern1 = r"(?P<hostname>an\S+.\S+.\S+)#"
    pattern2 = r"(?P<interface>Twe\S+).+\W*\d+\.\d+ +\W*\d+\.\d+ +\W*\d+\.\d+ +(?P<Tx_Power>\W*\d+\.\d+) +(?P<Rx_Power>\W*\d+\.\d+)"
    regex = f"{pattern1}|{pattern2}"
    with open(data) as f:
        result = []
        for line in f:
            match1 = re.search(pattern1, line)
            match2 = re.search(pattern2, line)
            if match1:
                result.append(match1.group('hostname'))
            elif match2:
                result.append(match2.group('interface'))
                result.append(match2.group('Tx_Power'))
                result.append(match2.group('Rx_Power'))
        output = [result[i:i+4] for i in range(0, len(result), 4)]
        for item in output:
            tx_power_a = round(float(item[3]) + 0.6, 1)
            item.append(str(tx_power_a))
            rx_power_a = round(float(item[2]) - 0.6, 1)
            item.append(str(rx_power_a))
            item.append(item[2] + '/' + item[3])
            del item[2]
            del item[2]
            item.append(item[2] + '/' + item[3])
            del item[2]
            del item[2]

    return output

def write_inventory_to_csv(data_filenames, csv_filename):
    '''
    Функция имеет два параметра:
     * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
     * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
       в который будет записана информация в формате CSV
    * функция записывает содержимое в файл, в формате CSV и ничего не возвращает
    '''
    headers = ["hostname", "interface", "Tx_Power_B/Rx_Power_B", "Tx_Power_A/Rx_Power_A"]

    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for filename in data_filenames:
            lst_data = signal_levels(filename)
            for lst in lst_data:
                hostname, interface, tx_rx_b, tx_rx_a = lst
                writer.writerow((hostname, interface, tx_rx_b, tx_rx_a))


if __name__ == "__main__":
    data_filenames = glob.glob("signal_levels_*") #список из 2-х файлов signal_levels_KSK.txt, signal_levels_NSK.txt
    write_inventory_to_csv(data_filenames, 'sbc_power.csv')
    print('Результат сохранен в файл sbc_power.csv')









