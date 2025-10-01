# -*- coding: utf-8 -*-

# username_passwd = [{'username': 'cisco', 'password': 'cisco'},
#                    {'username': 'nata', 'password': 'natapass'},
#                    {'username': 'user', 'password': '123456789'}]


# def check_passwd(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print('Пароль слишком короткий')
#         return False
#     elif check_username and username in password:
#         print('Пароль содержит имя пользователя')
#         return False
#     else:
#         print(f'Пароль для пользователя {username} прошел все проверки')
#         return True

# for data in username_passwd:
#     check_passwd(**data)
list_vlan = [111, 130]
new_list = list(map(str, list_vlan))
print(new_list)
