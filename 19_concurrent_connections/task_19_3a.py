# -*- coding: utf-8 -*-
"""
Задание 19.3a

Создать функцию send_command_to_devices, которая отправляет список указанных
команд show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какие команды. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом каждой
команды надо написать имя хоста и саму команду):

R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R1#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
R3#sh ip route | ex -

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0


Для выполнения задания можно создавать любые дополнительные функции,
а также использовать функции созданные в предыдущих заданиях.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml
commands = {
    "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
    "192.168.100.1": ["sh ip int br", "sh int desc"],
    "192.168.100.2": ["sh int desc"],
}

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml
# commands = {
#     "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
#     "192.168.100.1": ["sh ip int br", "sh int desc"],
#     "192.168.100.2": ["sh int desc"],
# }


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
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

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
def send_command_to_devices(devices, commands_dict, filename, limit=3):
    '''
    Функция, которая отправляет список указанных команд show на разные устройства в параллельных потоках,
    а затем записываетвывод команд в файл.
    Параметры функции:
       * devices - список словарей с параметрами подключения к устройствам
       * commands_dict - словарь в котором указано на какое устройство отправлять какую команду.
       * filename - имя текстового файла, в который будут записаны выводы всех команд
       * limit - максимальное количество параллельных потоков (по умолчанию 3)
    '''
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(send_show_command, device, show) for device in devices for show in commands[device["host"]]]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())
    print("### Все потоки отработали")
    print(f'Результаты сохранены в файл {filename}')


if __name__ == "__main__":
    commands = {
    "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
    "192.168.100.1": ["sh ip int br", "sh int desc"],
    "192.168.100.2": ["sh int desc", "sh clock"]}

    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    send_command_to_devices(devices, commands, 'commands_all.txt', limit=2)

