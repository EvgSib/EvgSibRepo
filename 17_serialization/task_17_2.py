# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv
from pprint import pprint

def parse_sh_version(file_config):
    '''
    Данная функция:
    * ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
    * обрабатывает вывод, с помощью регулярных выражений
    * возвращает кортеж из трёх элементов:
     * ios - в формате "12.4(5)T"
     * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
     * uptime - в формате "5 days, 3 hours, 3 minutes"
    '''
    regex = (r'Cisco IOS Software, .+ Version (?P<ios>\S+),'
         r'|router uptime is (?P<uptime>\d+ \S+ \d+ \S+ \d+ \S+)'
         r'|System image file is (?P<image>\S+)')
    result = []
    with open(file_config) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.group(match.lastgroup))
    return tuple(result)


def write_inventory_to_csv(data_filenames, csv_filename):
    '''
    Функция имеет два параметра:
     * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
     * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
       в который будет записана информация в формате CSV
    * функция записывает содержимое в файл, в формате CSV и ничего не возвращает
    '''
    headers = ["hostname", "ios", "image", "uptime"]

    with open(csv_filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(headers)
        for filename in data_filenames:
            hostname = re.search("sh_version_(\S+).txt", filename).group(1)
            ios, uptime, image = parse_sh_version(filename)
            writer.writerow((hostname, ios, image, uptime))

if __name__ == "__main__":
    data_filenames = glob.glob("sh_version_*") #список из 3-х файлов sh_version_r1.txt, sh_version_r2.txt,sh_version_r3.txt
    print(data_filenames)
    write_inventory_to_csv(data_filenames, 'routers_inventory.csv')



