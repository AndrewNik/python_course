# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
	def merge(left, right):
		result = []
		i = j = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:] + right[j:]
		return result

	if len(arr) < 2:
		return arr
	else:
		l_side = arr[:len(arr) // 2]
		r_side = arr[len(arr) // 2:]
	return merge(merge_sort(l_side), merge_sort(r_side))


array = [i for i in range(0, 50)]
random.shuffle(array)
print(f'Исх. массив: {array}\nОтсортированный: {merge_sort(array)}')
