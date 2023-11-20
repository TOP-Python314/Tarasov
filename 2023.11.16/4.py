input = int(input("Введите число: "))
num = input // 10
num_1 = num // 10
num_2 = num % 10
num_3 = input % 10

print(
    f'Сумма цифр = {num_1 + num_2 + num_3}',
    f'Произведение цифр = {num_1 * num_2 * num_3}', sep='\n')

#Вывод
#Введите число: 123
#Сумма цифр = 6
#Произведение цифр = 6
