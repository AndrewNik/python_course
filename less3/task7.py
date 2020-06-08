# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

list1 = [random.randint(1, 100) for _ in range(20)]
print(list1)

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

print(f'1 мин. элемент: {fst_min}, 2 мин. элемент: {snd_min}')



