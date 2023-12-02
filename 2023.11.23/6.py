coordinates_1 = input("Введите координаты: ")
coordinates_2 = input("Введите координаты: ")

if ord(coordinates_1[0]) - 1 <= ord(coordinates_2[0]) <= ord(coordinates_1[0]) + 1 and int(coordinates_1[1]) - 1 <= int(coordinates_2[1]) <= int(coordinates_1[1]) + 1:
    print('да')

else:
    print('нет')
    
# Ввод:

# Введите координаты: g2
# Введите координаты: f1

# Вывод:

# да

# Ввод:

# Введите координаты: a1
# Введите координаты: b3

# Вывод:

# нет

