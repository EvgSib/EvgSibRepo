"""
Используя подготовленную строку nat, получить новую строку,
в которой в имени интерфейса вместо FastEthernet написано
GigabitEthernet. Полученную новую строку вывести на стандартный
поток вывода (stdout) с помощью print
"""
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
result = nat.replace('FastEthernet', 'GigabitEthernet')

print(result)
