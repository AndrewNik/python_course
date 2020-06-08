# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

list1 = [random.randint(-100, 100) for _ in range(20)]
print(list1)

max_neg_el = 0
neg_idx = -1

for idx, el in enumerate(list1):
	if el < 0 and (neg_idx == -1 or el > max_neg_el):
		max_neg_el = el
		neg_idx = idx

if max_neg_el < 0:
	print(f'Максимальный отрицательный элемент: {max_neg_el}, его индекс {neg_idx}')
else:
	print('Отрицательных элементов нет')