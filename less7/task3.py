# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

arr = [random.randint(0, 100) for i in range(2 * int(input('Введите m: ')) + 1)]

def quickselect_median(l):
	def quickselect(l, k):
		if len(l) == 1:
			assert k == 0
			return l[0]

		pivot = random.choice(l)

		lows = [el for el in l if el < pivot]
		highs = [el for el in l if el > pivot]
		pivots = [el for el in l if el == pivot]

		if k < len(lows):
			return quickselect(lows, k)
		elif k < len(lows) + len(pivots):
			return pivots[0]
		else:
			return quickselect(highs, k - len(lows) - len(pivots))

	return quickselect(l, len(l) / 2)


print(f'В массиве {arr} медиана: {quickselect_median(arr)}.')