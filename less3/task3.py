# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

list1[min_idx], list1[max_idx] = max_el, min_el
print(list1)
