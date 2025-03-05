# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""

# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

from concurrent.futures import ThreadPoolExecutor
import time
import random
from itertools import repeat
from datetime import datetime
import logging
import netmiko
import yaml


logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.getLogger("netmiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO
)


def send_show_command(device, show):
    '''
    Функция, которая подключается к устройству и отправляет одну команду show.
    Параметры функции:
       * device - словареь с параметрами подключения к устройству
       * show - команда
    '''
    host = device['host']
    logging.info(f">>> Подключаюсь к {host}")
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        hostname = ssh.find_prompt()
        send_command = ssh.send_command(show)
        output = f"\n{hostname}#{show}\n" + send_command
        logging.debug(f"\n{output}\n")
        logging.info(f"<<< Получена информация от {host}")
        return output


def send_show_to_devices(devices, command, filename, limit=3):
    '''
    Функция, которая отправляет одну и ту же команду show на разные устройства в параллельных потоках, а затем записывает
    вывод команд в файл.
    Параметры функции:
       * devices - список словарей с параметрами подключения к устройствам
       * command - команда
       * filename - имя текстового файла, в который будут записаны выводы всех команд
       * limit - максимальное количество параллельных потоков (по умолчанию 3)
    '''
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(send_show_command, devices, repeat(command))
        with open(filename, "w") as f:
            for output in results:
                f.write(output)
    print("### Все потоки отработали")
    print(f'Результаты сохранены в файл {filename}')


if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    send_show_to_devices(devices, "sh ip int br", 'sh_ip_int_br_all.txt', limit=2)

# def send_show_to_devices(devices, command, filename, limit=3):
#     with ThreadPoolExecutor(max_workers=limit) as executor:
#         results = executor.map(send_show_command, devices, repeat(command))
#         with open(filename, "w") as f:
#             for dev, output in zip(devices, results):
#                 f.write(output)
#     print("### Все потоки отработали")
#     print(f'Результаты сохранены в файл {filename}')
