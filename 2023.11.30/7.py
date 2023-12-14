text = input('Введите текст: ')

whitespace = set('.,:;!?–—\'\"()*/')

sorted = ''.join(word for word in text if word not in whitespace)

print(sorted)

# Ввод:

# Введите текст: Но всё, что мне мешало, я давно оставил.

# Вывод:

# Но всё что мне мешало я давно оставил

