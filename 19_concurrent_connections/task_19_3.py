# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_command_to_devices, которая отправляет разные
команды show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом
команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml
#     commands = {
#     "192.168.100.1": "sh ip int br",
#     "192.168.100.2": "sh int desc",
#     "192.168.100.3": "sh run | s ^router ospf"}

from concurrent.futures import ThreadPoolExecutor, as_completed
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
        output = f"\n{hostname}{show}\n" + send_command
        logging.debug(f"\n{output}\n")
        logging.info(f"<<< Получена информация от {host}")
        return output

#этот вариант функции использует executor.submit, поэтому вывод может быть в произвольном порядке.
#ниже закомментированный вариант функции send_command_to_devices с executor.map, там вывод будет по порядку
def send_command_to_devices(devices, commands_dict, filename, limit=3):
    '''
    Функция которая отправляет разные команды show на разные устройства в параллельных потоках,
    а затем записывает вывод команд в файл.
    Параметры функции:
       * devices - список словарей с параметрами подключения к устройствам
       * commands_dict - словарь в котором указано на какое устройство отправлять какую команду.
       * filename - имя текстового файла, в который будут записаны выводы всех команд
       * limit - максимальное количество параллельных потоков (по умолчанию 3)
    '''
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(send_show_command, device, commands_dict[device["host"]]) for device in devices]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())
    print("### Все потоки отработали")
    print(f'Результаты сохранены в файл {filename}')

if __name__ == "__main__":
    commands = {
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh int desc",
    "192.168.100.3": "sh run | s ^router ospf"}

    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, commands, 'commands_all.txt', limit=2)

# logging.getLogger("paramiko").setLevel(logging.WARNING)
# logging.getLogger("netmiko").setLevel(logging.WARNING)

# logging.basicConfig(
#     format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
#     level=logging.INFO
# )


# def send_show_command(device, show):
#     '''
#     Функция, которая подключается к устройству и отправляет одну команду show.
#     Параметры функции:
#        * device - словареь с параметрами подключения к устройству
#        * show - команда
#     '''
#     host = device['host']
#     logging.info(f">>> Подключаюсь к {host}")
#     with netmiko.ConnectHandler(**device) as ssh:
#         ssh.enable()
#         hostname = ssh.find_prompt()
#         send_command = ssh.send_command(show)
#         output = f"\n{hostname}{show}\n" + send_command
#         logging.debug(f"\n{output}\n")
#         logging.info(f"<<< Получена информация от {host}")
#         return output


# def send_command_to_devices(devices, commands_dict, filename, limit=3):
#     '''
#     Функция которая отправляет разные команды show на разные устройства в параллельных потоках,
#     а затем записывает вывод команд в файл.
#     Параметры функции:
#        * devices - список словарей с параметрами подключения к устройствам
#        * commands_dict - словарь в котором указано на какое устройство отправлять какую команду.
#        * filename - имя текстового файла, в который будут записаны выводы всех команд
#        * limit - максимальное количество параллельных потоков (по умолчанию 3)
#     '''
#     with ThreadPoolExecutor(max_workers=limit) as executor:
#         list_commands = [command for command in commands.values()]
#         results = executor.map(send_show_command, devices, list_commands)
#         with open(filename, "w") as f:
#             for output in results:
#                 f.write(output)
#     print("### Все потоки отработали")
#     print(f'Результаты сохранены в файл {filename}')


# if __name__ == "__main__":
#     commands = {
#     "192.168.100.1": "sh ip int br",
#     "192.168.100.2": "sh int desc",
#     "192.168.100.3": "sh run | s ^router ospf"}

#     with open('devices.yaml') as f:
#         devices = yaml.safe_load(f)
#     send_command_to_devices(devices, commands, 'commands_all.txt', limit=2)

