'''
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

custom_list = []

while len(custom_list) < 10:
    list_element = input('please enter the custom list element: ')
    custom_list.append(list_element)

# print(custom_list)

# custom_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

for i in range(0, len(custom_list), 2):
    if i < len(custom_list) - 1:

        val_one = custom_list[i]
        val_two = custom_list[i+1]
        
        custom_list[i] = val_two
        custom_list[i+1] = val_one
        
print(custom_list)