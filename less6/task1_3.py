# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

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
def double_min(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	print(f'Размер формируемого списка: {sys.getsizeof(list1)}, содержимое списка занимает {obj_size(list1)}')
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


@mem_decorator
def double_min_easy_way(list_size):
	list1 = [random.randint(1, 100) for _ in range(list_size)]
	print(f'Размер формируемого списка: {sys.getsizeof(list1)}, содержимое списка занимает {obj_size(list1)}')
	fst_min = min(list1)
	list1.remove(fst_min)
	return fst_min, min(list1)


double_min(100)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции double_min: ((100,), {})
# Размер формируемого списка: 460, содержимое списка занимает 1400
# Функция: double_min вернула результат размером 36

double_min_easy_way(100)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции double_min_easy_way: ((100,), {})
# Размер формируемого списка: 460, содержимое списка занимает 1400
# Функция: double_min_easy_way вернула результат размером 36