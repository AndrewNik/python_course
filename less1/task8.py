# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = input('Введите 3 числа через запятую: ').split(',')
a, b, c = int(a), int(b), int(c)

if (a > b and a < c) or (a > c and a < b):
	print(f'Среднее {a}')
elif (b > a and b < c) or (b > c and b < a):
	print(f'Среднее {b}')
else:
	print(f'Среднее {c}')