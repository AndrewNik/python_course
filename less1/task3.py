# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

type = input('Введите режим работы (i-целое,f-вещественное,a-символ) ')
l_border, r_border = input('Введите границы диапазона через запятую ').split(',')

if type == 'i':
	res = random.randint(int(l_border), int(r_border))
	print(res)
elif type == 'f':
	res = random.uniform(float(l_border), float(r_border))
	print(res)
elif type == 'a':
	l_border, r_border = ord(l_border), ord(r_border)
	res = random.randint(l_border, r_border)
	res = chr(res)
	print(res)
else:
	print('Неверный режим работы')
