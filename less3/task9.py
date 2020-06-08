# 9. Найти максимальный элемент среди минимальных элементов строк матрицы.

import random

matrix = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

print(matrix)
min_list = []

for row in matrix:
	min_el = row[0]
	for el in row:
		if el < min_el:
			min_el = el
	min_list.append(min_el)

max_min = min_list[0]
for el in min_list:
	if el > max_min:
		max_min = el

print(f'Макс. среди минимальных {max_min}')