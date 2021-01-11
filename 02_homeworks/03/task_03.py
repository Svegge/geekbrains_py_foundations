'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''

def my_func(first, second, third):
    arg_list = [first, second, third]
    arg_list.sort(reverse=True)
    result = arg_list[0] + arg_list[1]
    return result

result = my_func(1200, 123, 100)
print(result)
