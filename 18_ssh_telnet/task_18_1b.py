# -*- coding: utf-8 -*-
"""
Задание 18.1b

Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется при ошибке
аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес
устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

import yaml
from netmiko import (ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException)

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

    except NetmikoTimeoutException:
        print(f'''TCP-подключение к устройству не удалось.

Обычные причины этой проблемы:
1. Неправильное имя хоста или IP-адрес.
2. Неправильный TCP-порт.
3. Промежуточный брандмауэр блокирует доступ''')

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        hostname = dev['host']
        print(f'*****вывод команды <<{command}>> для хоста {hostname}*****')
        print(send_show_command(dev, command))
        print('')
