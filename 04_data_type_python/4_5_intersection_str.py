"""
Из строк command1 и command2 получить список VLANов, которые есть и в
команде command1 и в команде command2 (пересечение).
В данном случае, результатом должен быть такой список: ['1', '3', '8']
Записать итоговый список в переменную result. (именно эта переменная
будет проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout)
с помощью print.
"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1_1 = command1.split()[-1].split(',')
command2_1 = command2.split()[-1].split(',')
result_set = set(command1_1) & set(command2_1)
result = sorted(list(result_set))
print(result)
