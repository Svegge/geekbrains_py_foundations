'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

stop_marker = None

def convert_user_string(list_of_numbers):
    list_of_strings = list_of_numbers.split()
    list_of_numbers = []
    for n in list_of_strings:
        list_of_numbers.append(int(n))
    return(list_of_numbers)
    


while stop_marker != '/':

    user_string = input('Please input number row if need stop enter "/": ')
