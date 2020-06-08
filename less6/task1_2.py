# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import sys

print(sys.version, sys.platform)


def mem_decorator(func):
	def wrapper(*args, **kwargs):
		print(f'Входные аргументы для функции {func.__name__}: {args, kwargs}')
		result = func(*args, **kwargs)
		print(f'Функция: {func.__name__} вернула результат размером {sys.getsizeof(result)}')

	return wrapper


def obj_size(obj):
	if isinstance(obj, list):
		return sum(map(sys.getsizeof, obj))


@mem_decorator
def sum_between_min_max(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	print(f'Размер формируемого списка: {sys.getsizeof(list1)}, содержимое списка занимает {obj_size(list1)}')
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


@mem_decorator
def sum_between_min_max_easy_way(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	print(f'Размер формируемого списка: {sys.getsizeof(list1)}, содержимое списка занимает {obj_size(list1)}')
	max_idx = list1.index(max(list1))
	min_idx = list1.index(min(list1))
	if max_idx < min_idx:
		min_idx, max_idx = max_idx, min_idx

	return sum(list1[min_idx + 1: max_idx])


sum_between_min_max(50)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции sum_between_min_max: ((50,), {})
# Размер формируемого списка: 268, содержимое списка занимает 700
# Функция: sum_between_min_max вернула результат размером 14

sum_between_min_max_easy_way(50)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции sum_between_min_max_easy_way: ((50,), {})
# Размер формируемого списка: 268, содержимое списка занимает 700
# Функция: sum_between_min_max_easy_way вернула результат размером 14
