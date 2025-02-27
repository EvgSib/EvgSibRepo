# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt
и данных из файла data_files/for.yml.

"""
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

from jinja2 import Environment, FileSystemLoader
import yaml
import os

# скрипт запустится из терминала. Пример передачи ему строки
#$ python cfg_gen.py templates/for.txt data_files/for.yml
def generate_config(template, data_dict):
    '''
    Функция возвращает строку с конфигурацией, которая была сгенерирована.
    Параметры функции:
        * template - путь к файлу с шаблоном (например, "templates/for.txt")
        * data_dict - словарь со значениями, которые надо подставить в шаблон
    '''
    template_dir, template_file = template.split('/')
    # Параметр trim_blocks удаляет первую пустую строку после блока конструкции, если его значение равно True (по умолчанию False)
    # Параметр lstrip_blocks контролирует то, будут ли удаляться пробелы и табы от начала строки до начала блока
    # (до открывающейся фигурной скобки).
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_file)

    return template.render(data_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yml" #это словарь со значениями переменных
    template_file = "templates/for.txt" #это шаблон конфигурации с переменными
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
