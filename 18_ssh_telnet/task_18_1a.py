# -*- coding: utf-8 -*-
"""
Задание 18.1a

Скопировать функцию send_show_command из задания 18.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется при ошибке аутентификации
на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
"""
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

import yaml
from netmiko import (ConnectHandler, NetmikoAuthenticationException)

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            return output
    except NetmikoAuthenticationException:
        print(f'''Ошибка аутентификации на устройстве.

Распространенные причины этой проблемы:
1. Неверное имя пользователя и пароль
2. Неверный файл SSH-ключа
3. Подключение к неправильному устройству {hostname}''')

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        hostname = dev['host']
        print(f'*****вывод команды <<{command}>> для хоста {hostname}*****')
        print(send_show_command(dev, command))
        print('')


# device = { "device_type": "cisco_ios",
#            "ip": "192.168.100.1",
#            "username": "cisco",
#            "password": "cisco",
#            "secret": "cisco"}

# command = 'sh ip int br'
