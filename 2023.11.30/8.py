number = int(input())
fib1 = fib2 = 1

if number == 1:
    print(fib1)
elif number == 0:
    print(0)
else:
    print(fib1, fib2, end=' ')

for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
    
# Ввод:

# 14

# Вывод:

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377