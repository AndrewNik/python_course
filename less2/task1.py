# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в
# качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), программа должна
# сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности
# деления на ноль, если он ввел его в качестве делителя.

while True:
	a, b = input('Введите 2 числа через запятую: ').split(',')
	a, b = int(a), int(b)
	operator = input('Введите знак операции или 0 для завершеняи работы: ')
	if operator not in ('0', '/', '+', '-', '*'):
		print('Неверный знак операции')
	elif operator == '0':
		break
	elif operator == '+':
		print(f'{a + b}')
	elif operator == '-':
		print(f'{a - b}')
	elif operator == '*':
		print(f'{a * b}')
	elif b == 0:
		print('Ошибка деления на 0')
	else:
		print(f'{a / b}')
