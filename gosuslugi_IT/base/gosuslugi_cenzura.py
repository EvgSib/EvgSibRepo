# -*- coding: utf-8 -*-
'''
БЫЛО
Описание:
Вы разрабатываете программу для фильтрации нецензурных выражений в соцсетях.
Требуется обработать строку таким образом, чтобы запрещенные слова в ней были заменены.

Формат ввода:
Две строки: одна – содержащая оригинальный текст, вторая – содержащая запрещённые слова,
разделённые запятыми. Входная строка содержит только буквы, пробелы и символы .?!,
Длина строк – от 10 до 250 символов.

Формат вывода:
Оригинальная строка, в которой все запрещенные слова заменены на
последовательность символов '#' совпадающей длины. Запрещенные слова заменяются
при полном совпадении без учёта регистра. Формы слов (например, «столы» и «стол»)
не учитываются и считаются разными словами.

Пример 1:
Входные данные:
кот, из-за которого пришлось купить новую посуду.
кот,новую

Выходные данные:

###, из-за которого пришлось купить #### посуду.

Пример 2:
Входные данные:
Книга не показалась ему особенно занимательной, модерну он предпочитал постмодерн.
модерн,книга,особенно

Выходные данные:

##### не показалась ему ######## занимательной, ####### он предпочитал постмодерн.
'''
# вариант №4 (рабочий)
def censor(text: str, blacklist: str) -> str:
    blacklist = blacklist.split(',')
    final_words = []
    in_text = text.split()
    for word in in_text:
        if any(char in ".,!?" for char in word):
            separator = word[-1]
            word_split = word.split(separator)[0]
            if word_split.lower() in blacklist:
                final_words.append("*"*len(word_split)+separator)
            else:
                final_words.append(word_split+separator)
        elif word.lower() in blacklist:
            final_words.append("*"*len(word))
        else:
            final_words.append(word)

    return ' '.join(final_words)

text = input()
blacklist = input()
censored_text = censor(text, blacklist)
print(censored_text)


# не рабочий вариант
# def censor(text, blacklist):
#     """ Заменяет запрещённые слова звёздочками.
#     Args:
#         text (str): исходный текст;
#         blacklist (list): список запрещённых слов.
#     Returns:
#         str: отцензурированный текст.
#     """
#     words = text.split()
#     result = []
#     for word in words:
#       Отделяем знаки препинания для правильной замены. Это упрощённая версия, в реальности нужно использовать регулярные выражения.
#         prefix = ''
#         suffix = ''
#         while word and not word.isalnum():
#             prefix += word
#             word = word[1:]
#         while word and not word[-1].isalnum():
#             suffix = word[-1] + suffix
#             word = word[:-1]
#         Проверяем, является ли слово запрещённым (без учёта регистра)
#         if word.lower() in [w.lower() for w in blacklist]:
#             censored = '*' * len(word)
#             result.append(prefix + censored + suffix)
#         else:
#             result.append(prefix + word + suffix)
#     return ' '.join(result)

# text = input()
# blacklist = input()
# censored_text = censor(text, blacklist)
# print(censored_text)



# вариант №1
# def censor(text: str, blacklist: str) -> str:
#     blacklist = blacklist.split(',')
#     final_words = []
#     in_text = text.split()
#     for word in in_text:
#         for item in blacklist:
#             if item in word:
#                 final_words.append(word.replace(item, len(item)*'#'))
#                 continue
#             else:
#                 final_words.append(word)
#     return ' '.join(final_words)

# text = input()
# blacklist = input()
# censored_text = censor(text, blacklist)
# print(censored_text)


# вариант №2
# import re

# def censor(text: str, blacklist: str) -> str:
#     blacklist = blacklist.split(',')
#     final_words = []
#     in_text = text.split()
#     for word in in_text:
#         if any(char in ".,!?" for char in word):
#             separator = re.split(r'\w+', word)[1]
#             word_split = re.split('\\' + separator, word)[0]
#             if word_split.lower() in blacklist:
#                 final_words.append("*"*len(word_split)+',')
#             else:
#                 final_words.append(word_split+separator)
#         elif word.lower() in blacklist:
#             final_words.append("#"*len(word))
#         else:
#             final_words.append(word)

#     return ' '.join(final_words)

# text = input()
# blacklist = input()
# censored_text = censor(text, blacklist)
# print(censored_text)


# вариант №3 (рабочий)
# def censor(text: str, blacklist: str) -> str:
#     blacklist = blacklist.split(',')
#     final_words = []
#     in_text = text.split()
#     for word in in_text:
#         if any(char in ".,!?" for char in word):
#             if ',' in word:
#                 word_split = word.split(',')[0]
#                 if word_split.lower() in blacklist:
#                     final_words.append("*"*len(word_split)+',')
#                 else:
#                     final_words.append(word_split+',')
#             elif '.' in word:
#                 word_split = word.split('.')[0]
#                 if word_split.lower() in blacklist:
#                     final_words.append("*"*len(word_split)+'.')
#                 else:
#                     final_words.append(word_split+'.')
#             elif '!' in word:
#                 word_split = word.split('!')[0]
#                 if word_split.lower() in blacklist:
#                     final_words.append("*"*len(word_split)+'?')
#                 else:
#                     final_words.append(word_split+'!')
#             else:
#                 word_split = word.split('?')[0]
#                 if word_split.lower() in blacklist:
#                     final_words.append("*"*len(word_split)+'?')
#                 else:
#                     final_words.append(word_split+'?')
#         elif word.lower() in blacklist:
#             final_words.append("*"*len(word))
#         else:
#             final_words.append(word)

#     return ' '.join(final_words)

# text = input()
# blacklist = input()
# censored_text = censor(text, blacklist)
# print(censored_text)





