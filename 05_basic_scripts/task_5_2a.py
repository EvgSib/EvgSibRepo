# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip_template_ip_adress = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}
'''
ip_template_mask_dec = '''
Mask:
/{mask_dec}
'''
ip_template_mask_dec_bin = '''
{mask_1:<8}  {mask_2:<8}  {mask_3:<8}  {mask_4:<8}
{mask_1:<08b}  {mask_2:<08b}  {mask_3:<08b}  {mask_4:<08b}
'''

name_network = input('Введите имя сети: ')
name_network_split = name_network.split('/')
ip_split = name_network_split[0].split('.')
result_ip = [int(item) for item in ip_split]
result_ip_bin = '{0:>08b}{1:>08b}{2:>08b}{3:>08b}'.format(result_ip[0], result_ip[1], result_ip[2], result_ip[3])
mask_quan = int(name_network_split[1])
mask_without_host = result_ip_bin[0:mask_quan]
mask_bin_32 = '{:0<32}'.format(mask_without_host)
network_0_8 = mask_bin_32[0:8]
network_8_16 = mask_bin_32[8:16]
network_16_24 = mask_bin_32[16:24]
network_24_32 = mask_bin_32[24:32]
network_1_dec = int(network_0_8, 2)
network_2_dec = int(network_8_16, 2)
network_3_dec = int(network_16_24, 2)
network_4_dec = int(network_24_32, 2)
print(ip_template_ip_adress.format(network_1_dec, network_2_dec, network_3_dec, network_4_dec))

mask_dec_finish = ip_template_mask_dec.format(mask_dec = name_network_split[1])
print(mask_dec_finish)

mask_int = int(name_network_split[-1])
mask_bin = '1' * mask_int
mask_bin32 = '{:0<32}'.format(mask_bin)
mask_0_8 = mask_bin32[0:8]
mask_8_16 = mask_bin32[8:16]
mask_16_24 = mask_bin32[16:24]
mask_24_32 = mask_bin32[24:32]

mask_1_dec = int(mask_0_8, 2)
mask_2_dec = int(mask_8_16, 2)
mask_3_dec = int(mask_16_24, 2)
mask_4_dec = int(mask_24_32, 2)

print(ip_template_mask_dec_bin.format(mask_1=mask_1_dec, mask_2=mask_2_dec, mask_3 = mask_3_dec, mask_4 = mask_4_dec))
