# -*- coding: utf-8 -*-
'''
Обработка email-адресов
Описание:
Вы разрабатываете модуль для обработки текстовых данных.
Вам необходимо извлечь из текста список всех уникальных email-адресов.

Email-адрес считается допустимым, если он:
Содержит только латинские буквы (в любом регистре), цифры, символы .-_ и +.
Начинается с буквы или цифры.
Содержит один символ @.
Завершается одним из следующих способов: .ru, .com, .org или .net
Формат ввода: Одна строка текста произвольной длины до 1000 символов.

Формат вывода:
Если найдены email-адреса, каждый найденный адрес выводится на отдельной строке.
Если адресов не найдено, выводится «Не найдено».

Пример 1:
Входные данные:
Это текст с email user123@example.com и user456@email.ru, но не example.com или sib23@mail.ru и sib23@mail.ru

Выходные данные:
user123@example.com
user456@email.ru
sib23@mail.ru

Пример 2:
Входные данные:
Это пример текста с невалидными адресами: +user@domain.com, +user@dom@in.com, user@domain.tv

Выходные данные:
Не найдено
'''

import re

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        list_email = re.findall(r'\S+\.?\S+@\S+\.\S+', self.text)
        middle_list = []
        for item in list_email:
            if item[-1] in ',.!?':
                middle_list.append(item[:-1])
            else:
                middle_list.append(item)
        result = []
        for item in middle_list:
            if item[0].isalnum() and item.count('@') == 1 and item.endswith(('.ru', '.com', '.org', '.net')):
                result.append(item)
        if result:
            result = set(result)
            for m in result:
                print(m)
        else:
            print('Не найдено')

input_text = input()
mail = TextProcessor(input_text)
mail.extract_emails()
