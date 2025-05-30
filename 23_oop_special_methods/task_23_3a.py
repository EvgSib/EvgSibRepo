# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""

from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def __getitem__(self, index):
        dict_output = list(self.topology.items())
        return dict_output[index]

    def __iter__(self):
        '''
        Если у объекта есть метод __iter__, итерируемый объект превращается в итератор вызовом
        iter(name), где name - имя итерируемого объекта. Если метода __iter__ нет, Python переби-
        рает элементы используя __getitem__.
        '''
        print('Вызываю __iter__')
        return iter(self.topology.items())

    def __add__(self, other):
        copy_topology = self.topology.copy()
        copy_topology.update(other.topology)
        return Topology(copy_topology)

    def _normalize(self, topology_dict):
        normalized_topology = {}
        for box, neighbor in topology_dict.items():
            if not neighbor in normalized_topology:
                normalized_topology[box] = neighbor
        return normalized_topology

    def delete_link(self, from_port, to_port):
        if from_port in self.topology and self.topology[from_port] == to_port:
            del self.topology[from_port]
        elif to_port in self.topology and self.topology[to_port] == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")

    def delete_node(self, node):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node in src or node in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")

    def add_link(self, src, dest):
        keys_and_values = set(self.topology.keys()) | set(self.topology.values())
        if self.topology.get(src) == dest or self.topology.get(dest) == src:
            print("Такое соединение существует")
        elif src in keys_and_values or dest in keys_and_values:
            print("Cоединение с одним из портов существует")
        else:
            self.topology[src] = dest

if __name__ == "__main__":
    topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

    print('Экземпляр t1')
    t1 = Topology(topology_example)
    for link in t1:
        print(link)
