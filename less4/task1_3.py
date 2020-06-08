# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random
import cProfile


def double_min(list_size):
	list1 = [random.randint(1, 100) for _ in range(20)]

	if list1[0] < list1[1]:
		fst_min, snd_min = list1[0], list1[1]
	else:
		fst_min, snd_min = list1[1], list1[0]

	for el in list1[2:]:
		if el < fst_min:
			if fst_min < snd_min:
				snd_min = fst_min
			fst_min = el
		elif el < snd_min:
			snd_min = el

	return fst_min, snd_min


def double_min_easy_way(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	fst_min = min(list1)
	list1.remove(fst_min)
	return fst_min, min(list1)

# "task3.double_min(50)"
# 1000 loops, best of 3: 66.4 usec per loop

# "task3.double_min(100)"
# 1000 loops, best of 3: 130 usec per loop

# "task3.double_min(1000)"
# 1000 loops, best of 3: 1.3 msec per loop

# "task3.double_min(10000)"
# 1000 loops, best of 3: 13.5 msec per loop

#   1    0.000    0.000    0.000    0.000 task3.py:7(double_min)
