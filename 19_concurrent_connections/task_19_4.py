# -*- coding: utf-8 -*-
"""
Задание 19.4

Создать функцию send_commands_to_devices, которая отправляет команду show или config
на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* filename - имя файла, в который будут записаны выводы всех команд
* show - команда show, которую нужно отправить (по умолчанию, значение None)
* config - команды конфигурационного режима, которые нужно отправить (по умолчанию None)
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Аргументы show, config и limit должны передаваться только как ключевые. При передачи
этих аргументов как позиционных, должно генерироваться исключение TypeError.

In [4]: send_commands_to_devices(devices, 'result.txt', 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands_to_devices(devices, 'result.txt', 'sh clock')

TypeError: send_commands_to_devices() takes 2 positional argument but 3 were given


При вызове функции send_commands_to_devices, всегда должен передаваться
только один из аргументов show, config. Если передаются оба аргумента, должно
генерироваться исключение ValueError.


Вывод команд должен быть записан в файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Пример вызова функции:
In [5]: send_commands_to_devices(devices, 'result.txt', show='sh clock')

In [6]: cat result.txt
R1#sh clock
*04:56:34.668 UTC Sat Mar 23 2019
R2#sh clock
*04:56:34.687 UTC Sat Mar 23 2019
R3#sh clock
*04:56:40.354 UTC Sat Mar 23 2019

In [11]: send_commands_to_devices(devices, 'result.txt', config='logging 10.5.5.5')

In [12]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.5.5.5
R1(config)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#logging 10.5.5.5
R2(config)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#logging 10.5.5.5
R3(config)#end
R3#

In [13]: commands = ['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0']

In [13]: send_commands_to_devices(devices, 'result.txt', config=commands)

In [14]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router ospf 55
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#router ospf 55
R2(config-router)#network 0.0.0.0 255.255.255.255 area 0
R2(config-router)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#router ospf 55
R3(config-router)#network 0.0.0.0 255.255.255.255 area 0
R3(config-router)#end
R3#


Для выполнения задания можно создавать любые дополнительные функции.
"""
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

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

def send_config_commands(device, config_commands):
    host = device['host']
    logging.info(f">>> Подключаюсь к {host}")
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        hostname = ssh.find_prompt()
        result = ssh.send_config_set(config_commands)
        output = f"\n{result}"
        logging.debug(f"\n{output}\n")
        logging.info(f"<<< Получена информация от {host}")
    return output

def send_show_command(device, show):
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

def send_command_to_devices(devices, filename, commands_list_show=None, commands_list_config=None, limit=3):
    '''
    Функция, которая отправляет список указанных команд show или config на разные устройства в параллельных потоках,
    а затем записывает вывод команд в файл.
    Параметры функции:
       * devices - список словарей с параметрами подключения к устройствам
       * commands_list_show - список команд show, в котором указано на какое устройство отправлять какую команду.
       * commands_list_config - список команд config, в котором указано на какое устройство отправлять какую команду.
       * filename - имя текстового файла, в который будут записаны выводы всех команд
       * limit - максимальное количество параллельных потоков (по умолчанию 3)
    '''
    with ThreadPoolExecutor(max_workers=limit) as executor:
        if commands_list_show:
            futures = [executor.submit(send_commands, device, show) for device in devices for show in commands_list_show]
            with open(filename, "w") as f:
                for future in as_completed(futures):
                    f.write(future.result())
        elif commands_list_config:
            results = executor.map(send_config_commands, devices, repeat(commands_list_config))
            with open(filename, "w") as f:
                for output in results:
                    f.write(output)
    print("### Все потоки отработали")
    print(f'Результаты сохранены в файл {filename}')

#функция из нашего задания 19.4
def send_commands_to_devices(devices, filename, *, config=None, show=None, limit = 3):
    '''
    Функция, которая отправляет команду show или config на разные устройства в параллельных потоках,
    а затем записывает вывод команд в файл.
    Параметры функции:
        * devices - список словарей с параметрами подключения к устройствам
        * filename - имя файла, в который будут записаны выводы всех команд
        * show - команда show, которую нужно отправить (по умолчанию, значение None)
        * config - команды конфигурационного режима, которые нужно отправить (по умолчанию None)
        * limit - максимальное количество параллельных потоков (по умолчанию 3)
    Аргументы show, config и limit должны передаваться только как ключевые.
    '''
    if show and config:
        raise ValueError("Можно передавать только один из аргументов show/config")
    elif show:
        send_command_to_devices(devices, filename, commands_list_show=show, limit=limit)
    elif config:
        send_command_to_devices(devices, filename, commands_list_config=config, limit=limit)


if __name__ == "__main__":
    commands_config = ["router ospf 55", "network 0.0.0.0 255.255.255.255 area 0"]
    commands_show = ["sh ip int br", "sh ip route", "sh clock"]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
#         send_commands_to_devices(devices, 'commands_all.txt', show=commands_show, limit = 2)
        send_commands_to_devices(devices, 'commands_all.txt', config=commands_config, limit = 2)

#ниже решение Н.Самойленко (поизящнее)
# from itertools import repeat
# from concurrent.futures import ThreadPoolExecutor, as_completed

# from netmiko import ConnectHandler, NetMikoTimeoutException
# import yaml


# def send_show_command(device, command):
#     with ConnectHandler(**device) as ssh:
#         ssh.enable()
#         result = ssh.send_command(command)
#         prompt = ssh.find_prompt()
#     return f"{prompt}{command}\n{result}\n"


# def send_cfg_commands(device, commands):
#     with ConnectHandler(**device) as ssh:
#         ssh.enable()
#         result = ssh.send_config_set(commands)
#     return f"{result}\n"


# def send_commands_to_devices(devices, filename, *, show=None, config=None, limit=3):
#     if show and config:
#         raise ValueError("Можно передавать только один из аргументов show/config")
#     command = show if show else config
#     function = send_show_command if show else send_cfg_commands

#     with ThreadPoolExecutor(max_workers=limit) as executor:
#         futures = [executor.submit(function, device, command) for device in devices]
#         with open(filename, "w") as f:
#             for future in as_completed(futures):
#                 f.write(future.result())


# if __name__ == "__main__":
#     command = "sh ip int br"
#     with open("devices.yaml") as f:
#         devices = yaml.load(f)
#     send_commands_to_devices(devices, show=command, filename="result.txt")
#     send_commands_to_devices(devices, config="logging 10.5.5.5", filename="result.txt")


