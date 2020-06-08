# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a, b, c = input('Введите длины отрезков через запятую: ').split(',')

a, b, c = int(a), int(b), int(c)
if a >= b + c or b >= a + c or c >= a + b:
	print('Треугольник не существует')
elif a == b == c:
	print('Треугольник равносторонний')
elif a != b and b != c and c != a:
	print('Треугольник разносторонний')
else:
	print('Треугольник равнобедренный')
