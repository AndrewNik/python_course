# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))

if year % 400 == 0:
	print('Високосный год')
elif year % 4 == 0 and year % 100 != 0:
	print('Високосный год')
else:
	print('Невисокосный год')