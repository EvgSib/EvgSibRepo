# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import re

class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании,
    возникла ошибка.
    Этот класс тупо наследует класс Exception и в выводе вместо Exception
    будет ErrorInCommand (мой комментарий)
    класс ErrorInCommand указывается после raise в функции _check_error_in_command
    """

class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, output):
        regex = "% (?P<err>.+)"
        template = (
            'При выполнении команды "{cmd}" на устройстве {device} '
            "возникла ошибка -> {error}"
        )
        error_in_cmd = re.search(regex, output)
        if error_in_cmd:
            message = template.format(cmd=command, device=self.host, error=error_in_cmd.group("err"))
            raise ErrorInCommand(message)

    def send_command(self, command, *args, **kwargs):
        output = super().send_command(command, *args, **kwargs)
        self._check_error_in_command(command, output)
        return output

    def send_config_set(self, config_commands, *args, **kwargs):
        if isinstance(config_commands, str):
            output = super().send_config_set(config_commands, *args, **kwargs)
            self._check_error_in_command(config_commands, output)
        elif isinstance(config_commands, list):
            output = ''
            for command in config_commands:
                output += super().send_config_set(command, exit_config_mode=False) #тут параметр exit_config_mode обязательно нужен, иначе выдаст ошибку
                self._check_error_in_command(command, output)
        return output
#     ниже решение Самойленко
#     def send_config_set(self, commands):
#         if isinstance(commands, str):
#             commands = [commands]
#         commands_output = ""
#         self.config_mode()
#         for command in commands:
#             result = super().send_config_set(command, exit_config_mode=False)
#             commands_output += result
#             self._check_error_in_command(command, result)
#         self.exit_config_mode()
#         return commands_output

if __name__ == "__main__":
    device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco"
    }

    r1 = MyNetmiko(**device_params)
    print(r1.send_config_set('int lo55'))
#     print(r1.send_config_set('int'))




