# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите число: '))
evens, odds = [], []

while num > 0:
	digit = num % 10
	if digit % 2 == 0:
		evens.append(digit)
	else:
		odds.append(digit)
	num //= 10

print(f'Нечетные: {odds}. Четные: {evens}')