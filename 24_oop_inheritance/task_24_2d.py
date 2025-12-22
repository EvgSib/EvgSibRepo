# -*- coding: utf-8 -*-

"""
Задание 24.2d

Скопировать класс MyNetmiko из задания 24.2c или задания 24.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен
работать точно так же как метод send_config_set в netmiko.
Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

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

    def send_config_set(self, commands, ignore_errors=True, *args, **kwargs):
        if ignore_errors:
            output = super().send_config_set(commands, *args, **kwargs)
            return output
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ""
        commands_output += self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output += result
            self._check_error_in_command(command, result)
        commands_output += self.exit_config_mode()
        return commands_output

if __name__ == "__main__":
    device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco"
    }

    r1 = MyNetmiko(**device_params)
    print(r1.send_config_set('lo', ignore_errors=True))
    print(r1.send_config_set('lo', ignore_errors=False))
