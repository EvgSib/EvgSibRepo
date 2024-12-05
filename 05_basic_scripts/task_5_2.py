# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


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
print(ip_template_ip_adress.format(result_ip[0], result_ip[1], result_ip[2], result_ip[3]))

mask_dec_finish = ip_template_mask_dec.format(mask_dec = name_network_split[1])

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
print(mask_dec_finish)
print(ip_template_mask_dec_bin.format(mask_1=mask_1_dec, mask_2=mask_2_dec, mask_3 = mask_3_dec, mask_4 = mask_4_dec))


