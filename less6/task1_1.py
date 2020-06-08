# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import sys

print(sys.version, sys.platform)


def mem_decorator(func):
	def wrapper(*args, **kwargs):
		print(f'Входные аргументы для функции {func.__name__}: {args, kwargs}')
		result = func(*args, **kwargs)
		print(f'Функция: {func.__name__} вернула результат размером {sys.getsizeof(result)}')

	return wrapper


@mem_decorator
def check_equation(n):
	sum = 0
	range_obj = range(1, n + 1)
	print(f'Размер формируемого массива: {sys.getsizeof(range_obj)}')
	for i in range_obj:
		sum += i
	return sum == n * (n + 1) / 2


@mem_decorator
def check_equation_easy_way(n):
	range_obj = range(1, n + 1)
	print(f'Размер формируемого массива: {sys.getsizeof(range_obj)}')
	return sum(range_obj) == n * (n + 1) / 2


check_equation(15)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции check_equation: ((15,), {})
# Размер формируемого массива: 24
# Функция: check_equation вернула результат размером 14

check_equation_easy_way(15)
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] win32
# Входные аргументы для функции check_equation_easy_way: ((15,), {})
# Размер формируемого массива: 24
# Функция: check_equation_easy_way вернула результат размером 14
