"""
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
„101010101010101010111011101110111100110011001100“
Полученную новую строку вывести на стандартный поток вывода (stdout)
с помощью print.
"""
mac = "AAAA:BBBB:CCCC"
mac_split = mac.split(':')
bin_mac = [bin(int(item, 16))[2:] for item in mac_split]
result = ''.join(bin_mac)
print(result)
