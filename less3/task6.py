# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list1 = [random.randint(1, 100) for _ in range(20)]
print(list1)

max_el, min_el = list1[0], list1[0]
max_idx, min_idx = 0, 0

for idx, el in enumerate(list1):
	if el > max_el:
		max_el = el
		max_idx = idx
	if el < min_el:
		min_el = el
		min_idx = idx

sum = 0
if max_idx < min_idx:
	min_idx, max_idx = max_idx, min_idx

for el in list1[min_idx + 1: max_idx]:
	sum += el

print(f'Сумма между мин. и макс. элементами: {sum}')
