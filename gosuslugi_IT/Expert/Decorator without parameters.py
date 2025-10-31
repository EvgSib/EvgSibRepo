# -*- coding: utf-8 -*-


def property(func):
    def wrapper(self):  # Важно: обёртка должна принимать `self`
        print("Декоратор: Выполняется код перед вызовом метода.")
        result = func(self)  # Вызов оригинального метода, передавая `self`
        print("Декоратор: Выполняется код после вызова метода.")
        return result
    return wrapper


class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = int(quantity)


    @property
    def quarter(self):
        month = int(self.date.split('-')[1])
        if 1 <= month <= 3:
            return "Q1"
        elif 4 <= month <= 6:
            return "Q2"
        elif 7 <= month <= 9:
            return "Q3"
        else:
            return "Q4"


def pusk():
    item = Item('2023-02-05', 'Шляпа', '4')
    quarter = item.quarter()
    print('the end')

pusk()
