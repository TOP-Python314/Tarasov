n = int(input('Введите целое число: '))
sum = 0

for j in range(1, n // 2 + 1):
	if n % j == 0:
		sum += j
print(sum + n)

# Ввод:

# Введите целое число: 15

# Вывод:

# 24