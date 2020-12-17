'''
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

start_result = int(input('Please, enter start result (km): '))
target_result = int(input('Please, enter target result (km): '))

current_result = start_result
days_counter = 1

while current_result <= target_result:
    print(f'{days_counter}-й день: {current_result}')
    current_result = round(current_result * 1.1, 2)
    days_counter = days_counter + 1

print(f'{days_counter}-й день: {current_result}')
print(f'Ответ: на {days_counter}-й день спортсмен достиг результата — не менее {target_result} км.')