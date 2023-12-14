ticket = input('Введите номер билета: ')
    
if len(ticket) != 6:
    print('error')
if len(ticket) == 6:
    if sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])):
        print('да')
    else:
        print('нет')

# Ввод:

# Введите номер билета: 123321

# Вывод:

# да

# Ввод:

# Введите номер билета: 123456

# Вывод:

# нет