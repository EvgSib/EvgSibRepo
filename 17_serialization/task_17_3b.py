# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

# не может импортировать модуль yaml
# чтобы скрипт запустился нужно скопировать его и файлы "draw_network_graph.py" в /home/python/venv/pyneng-py3-7/lib/python3.7/site-packages/

from pprint import pprint
import yaml
import glob
from draw_network_graph import draw_topology


def transform_topology(topology_filename):
    with open(topology_filename) as f:
        raw_topology = yaml.safe_load(f)

    formatted_topology = {}
    for l_device, peer in raw_topology.items():
        for l_int, remote in peer.items():
            r_device, r_int = list(remote.items())[0]
            if not (r_device, r_int) in formatted_topology:
                formatted_topology[(l_device, l_int)] = (r_device, r_int)
    return formatted_topology


if __name__ == "__main__":
    formatted_topology = transform_topology("topology.yaml")
    draw_topology(formatted_topology)


# def transform_topology(topology_yaml):
#     with open(topology_yaml) as f:
#         templates = yaml.safe_load(f)
#         topology_dict = {}
#         result = {}
#         for hostname, dict2 in templates.items():
#             for str_dict2 in dict2.items():
#                 port_id = list(str_dict2)[0]
#                 dict_l_intf_dev_id = list(str_dict2)[1]
#                 local_intf = list(dict_l_intf_dev_id.values())[0]
#                 device_id = list(dict_l_intf_dev_id.keys())[0]
#                 topology_dict[(hostname, port_id)] = (device_id, local_intf)
#         for line in topology_dict.items():
#             if not result.get(line[0]) and not result.get(line[1]):
#                 result[line[0]] = line[1]
#         return result

# if __name__ == "__main__":
#     topology_dict = transform_topology('topology.yaml')
#     print(topology_dict)
#     draw_topology(topology_dict)
