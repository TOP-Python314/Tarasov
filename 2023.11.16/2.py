# ПЕРЕИМЕНОВАТЬ: input — это имя встроенной функции, объявляя собственную переменную с таким именем вы теряете прямой доступ к встроенной функции
# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
# ИСПРАВИТЬ: преобразование во float избыточно, согласно условию должно быть введено целое число
num = int(input("Введите любое число: "))
print(
    f'Следующее за числом {num} число: {num + 1}',
    f'Для числа {num} предыдущее число: {num - 1}',
    sep='\n'
)


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий" или аналогичная
# ИСПОЛЬЗОВАТЬ везде: достаточно копировать содержимое терминала как есть: без изменений, дополнительных комментариев, отступов и т.п.
# Введите любое число: 20
# Следующее за числом 20 число: 21
# Для числа 20 предыдущее число: 19


# ИТОГ: хорошо, но можно лучше — 2/3
