message = input('Введите текст: ')

msg = message.split()
msg = ''.join(msg)

x = len(msg)

y = x * 30

price = f'{y // 100} руб. {y % 100} коп.'

print(price)

# Ввод: 

# Введите текст: Но осталось потерпеть

# Вывод:

# 5 руб. 70 коп.