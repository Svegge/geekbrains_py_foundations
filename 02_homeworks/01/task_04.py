'''4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

input_num = input('Please, enter any number: ')

count_numbers = len(input_num)

curr_num = 0

while curr_num == count_numbers:
    print(int(input_num[curr_num]))
    curr_num += 1