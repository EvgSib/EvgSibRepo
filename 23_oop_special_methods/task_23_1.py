# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""
class IPAddress:
    def __init__(self, ip_mask):
        ip_address, mask = ip_mask.split('/')
        self.ip_address = ip_address
        self.mask = mask
        self._check_ip(ip_address, mask)

    def _check_ip(self, ip_address, mask):
        octets = ip_address.split(".")
        correct_ip, correct_mask = [True,True]

        if len(octets) != 4:
            correct_ip = False
        elif not 8 <= int(mask) <= 32:
            correct_mask = False
        else:
            for octet in octets:
                # тут второе условие int(octet) in range(256)
                # проверяется только в том случае, если первое условие истина
                # Если встретился хоть один октет с нарушением,
                # дальше можно не смотреть
                    if not (octet.isdigit() and int(octet) in range(256)):
                        correct_ip = False
                        break
        if not correct_ip:
            raise ValueError(f"Неправильнo задан IP-адрес {ip_address}")
        elif not correct_mask:
            raise ValueError(f"Неправильнo задана маска {mask}")
        else:
            return True

if __name__ == "__main__":
    ip = IPAddress('10.1.1.1/24')
    print(ip)







