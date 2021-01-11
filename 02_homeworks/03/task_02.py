'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def user_data(name, lastname, birth_year, city, email, phone):
    print('User info:', name, lastname, birth_year, city, email, phone)

user_data(name='Karl', lastname='Barth', birth_year='1886', city='Basel', email='karl_barth@email.com', phone='99999999999')