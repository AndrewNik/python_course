# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import cProfile

def sum_between_min_max(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
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

	return sum

# "task2.sum_between_min_max(50)"
# 1000 loops, best of 3: 70 usec per loop

# "task2.sum_between_min_max(100)"
# 1000 loops, best of 3: 135 usec per loop

# "task2.sum_between_min_max(1000)"
# 1000 loops, best of 3: 1.4 msec per loop

# "task2.sum_between_min_max(10000)"
# 1000 loops, best of 3: 14 msec per loop

#  1    0.000    0.000    0.002    0.002 task2.py:7(sum_between_min_max)

def sum_between_min_max_easy_way(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	max_idx = list1.index(max(list1))
	min_idx = list1.index(min(list1))
	if max_idx < min_idx:
		min_idx, max_idx = max_idx, min_idx

	return sum(list1[min_idx + 1: max_idx])

# "task2.sum_between_min_max_easy_way(50)"
# 1000 loops, best of 3: 68.5 usec per loop

# "task2.sum_between_min_max_easy_way(100)"
# 1000 loops, best of 3: 136 usec per loop

# "task2.sum_between_min_max_easy_way(1000)"
# 1000 loops, best of 3: 1.37 msec per loop

# "task2.sum_between_min_max_easy_way(10000)"
# 1000 loops, best of 3: 13.5 msec per loop

# 1    0.000    0.000    0.002    0.002 task2.py:42(sum_between_min_max_easy_way)
