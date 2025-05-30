# -*- coding: utf-8 -*-
"""
Задание 20.4

Создайте шаблон templates/add_vlan_to_switch.txt, который будет использоваться
при необходимости добавить VLAN на коммутатор.

В шаблоне должны поддерживаться возможности:
* добавления VLAN и имени VLAN
* добавления VLAN как access, на указанном интерфейсе
* добавления VLAN в список разрешенных, на указанные транки

Шаблон надо создавать вручную.

Если VLAN необходимо добавить как access, надо настроить и режим интерфейса
и добавить его в VLAN:
interface Gi0/1
 switchport mode access
 switchport access vlan 5

Для транков, необходимо только добавить VLAN в список разрешенных:
interface Gi0/10
 switchport trunk allowed vlan add 5

Имена переменных надо выбрать на основании примера данных,
в файле data_files/add_vlan_to_switch.yaml.


Проверьте шаблон templates/add_vlan_to_switch.txt на данных
в файле data_files/add_vlan_to_switch.yaml, с помощью функции generate_config
из задания 20.1.
Не копируйте код функции generate_config.

"""
# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

from task_20_1 import generate_config
import yaml

# содержимое шаблона смотри в файле templates/add_vlan_to_switch.txt
if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml" #это словарь со значениями переменных
    template_file = "templates/add_vlan_to_switch.txt" #это шаблон конфигурации с переменными
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))

# шаблон выглядит так templates/ospf.txt




