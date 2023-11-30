input1 = input("Введите координаты: ")
input2 = input("Введите координаты: ")

sum1 = ord(input1[0]) + int(input1[1])
sum2 = ord(input2[0]) + int(input2[1])

if ord(input1[0]) >= ord('h') or ord(input2[0]) >= ord('h'):
    print('выходит за H')
    
   
if ord(input1[1]) >= int(ord('9')) or ord(input1[1]) >= int(ord('9')):
    print('больше 8')
    
    
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