"""
Список vlans это список VLANов, собранных со всех устройств сети, 
поэтому в списке есть повторяющиеся номера VLAN.
Из списка vlans нужно получить новый список уникальных номеров VLANов, 
отсортированный по возрастанию номеров. Для получения итогового списка 
нельзя удалять конкретные vlanы вручную.
Записать итоговый список уникальных номеров VLANов в переменную result. 
(именно эта переменная будет проверяться в тесте)
Полученный список result вывести на стандартный поток вывода (stdout) 
с помощью print.
"""
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

