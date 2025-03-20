# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""

class IPAddress:
    def __init__(self, ip_mask):
        ip_address, mask = ip_mask.split('/')
        self.ip_address = ip_address
        self.mask = mask
        self._check_ip(ip_address, mask)

    #отвечает за отображение информации
    def __str__(self):
        return f"IP address {self.ip_address}/{self.mask}"

    #также отвечает за отображение информации
    def __repr__(self):
        return f"IPAddress('{self.ip_address}/{self.mask}')"

    def _check_ip(self, ip_address, mask):
        octets = ip_address.split(".")
        correct_ip, correct_mask = [True,True]
        if len(octets) != 4:
            correct_ip = False
        elif not 8 <= int(mask) <= 32:
            correct_mask = False
        else:
            for octet in octets:
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
    ip1 = IPAddress('10.1.1.1/24')
    ip2 = IPAddress('7.7.7.7/24')
    ip_list = []
    ip_list.append(ip1)
    ip_list.append(ip2)
    print(ip_list)
