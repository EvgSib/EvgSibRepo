# -*- coding: utf-8 -*-
'''
Система управления доступом
Вы работаете над внутрикорпоративной системой доступа пользователей. Реализуйте класс UserManager,
который будет управлять доступом пользователей к системе.

У класса должны быть методы для добавления нового пользователя, удаления пользователя,
повышения и понижения уровня доступа пользователя, а также для получения списка всех пользователей.

Уровни доступа пользователей — это целые числа (0 ≤ x).
Класс UserManager должен поддерживать следующие методы, которые должны быть цепочками (кроме get_users):
add_user() — добавляет нового пользователя с указанным уровнем доступа или уровнем доступа по умолчанию, равным 1;
remove_user() — удаляет пользователя;
promote() — увеличивает уровень доступа пользователя на 1;
demote() — уменьшает уровень доступа на 1, если уровень доступа больше 0. Иначе ничего не происходит.
get_users() — вернет список всех пользователей с их текущим уровнем доступа.

Формат ввода
Несколько строк, состоящих из команд add_user, remove_user, promote, demote, get_users.
Входные данные гарантированно завершаются командой get_users.

Формат вывода
Несколько строк, в которой может быть один из вариантов:
Пользователи с уровнем доступа если введена команда get_users;
«‎Не найдено»‎, если пользователей в списке не осталось.

Пример 1 (тест):
Входные данные:
add_user Анна 1
add_user Борис 2
promote Анна
get_users

Выходные данные:
Анна: 2
Борис: 2

Пример 2 (тест):
Входные данные:
add_user Анна 3
add_user Борис 2
promote Анна
get_users
add_user Евгений 2

Выходные данные:
Анна: 4
Борис: 2

Пример 3 (тест):
Входные данные:
add_user Bob 3
add_user Charlie 2
remove_user Bob
remove_user Charlie
get_users

Выходные данные:
Не найдено

Пример 4 (тест):
Входные данные:
add_user Alice 4
add_user Bob 3
add_user Charlie 2
get_users

Выходные данные:
Alice: 4
Bob: 3
Charlie: 2

Пример 5 (тест):
Входные данные:
add_user Alice 1
add_user Bob 3
add_user Charlie 2
remove_user Bob
get_users

Выходные данные:
Alice: 1
Charlie: 2

Пример 6 (тест):
Входные данные:
add_user Alice 1
add_user Bob 3
add_user Charlie 3
promote Alice
promote Alice
demote Alice
get_users

Выходные данные:
Alice: 2
Bob: 3
Charlie: 3
'''

class UserManager:
   def __init__(self):
       self.users = {}

   def add_user(self, name, level=1):
       """
       Функция добавляет нового пользователя с указанным уровнем доступа
       или уровнем доступа по умолчанию, равным 1
       """
       self.users[name] = level

   def remove_user(self, name):
       """
       Функция удаляет пользователя
       """
       del self.users[name]

   def promote(self, name):
       """
       Функция увеличивает уровень доступа пользователя на 1
       """
       self.users[name] = self.users[name]+1

   def demote(self, name):
       """
       Функция уменьшает уровень доступа пользователя на 1,
       если уровень доступа больше 0. Иначе ничего не происходит.
       """
       if self.users[name] > 0:
           self.users[name] = self.users[name]-1

   def get_users(self):
       return self.users

user_manager = UserManager()
input_string = []
while True:
   try:
      line = input()
      if line == "":
         break
   except EOFError:
      break
   input_string.append(line)

for command in input_string:
    spl = command.split()
    if len(spl) == 1:
        metod = spl[0]
    elif len(spl) == 2:
        metod, name = spl[0], spl[1]
    else:
        metod, name, level = spl[0], spl[1], int(spl[2])
    if metod == 'add_user':
       user_manager.add_user(name, level)
    elif metod == 'remove_user':
       user_manager.remove_user(name)
    elif metod == 'promote':
       user_manager.promote(name)
    elif metod == 'demote':
       user_manager.demote(name)
    elif metod == 'get_users':
        d = user_manager.get_users()
        if d:
            for n, l in d.items():
                print(n + ': ' + str(l))
        else:
            print('Не найдено')



