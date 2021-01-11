'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def dev_two_numbers(first, second):
    if second != 0:
        result = first / second
    else:
        result = None
    return result

res = dev_two_numbers(14, 0)

print(res)
