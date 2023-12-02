coordinates_1 = input("Введите координаты: ")
coordinates_2 = input("Введите координаты: ")

sum1 = ord(coordinates_1[0]) + int(coordinates_1[1])
sum2 = ord(coordinates_2[0]) + int(coordinates_2[1])

if ord(coordinates_1[0]) >= ord('h') or ord(coordinates_2[0]) >= ord('h'):
    print('выходит за H')
    
   
if ord(coordinates_1[1]) >= int(ord('9')) or ord(coordinates_1[1]) >= int(ord('9')):
    print('выходит за 8')
    
    
if sum1 % 2 == sum2 % 2:
    print("да")
else:
    print("нет")
    
# Ввод:

# Введите координаты: b1
# Введите координаты: b3

# Вывод:

# да

# Ввод:

# Введите координаты: b2
# Введите координаты: b1

# Вывод:

# нет