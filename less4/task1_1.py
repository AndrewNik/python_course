# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import cProfile

def check_equation(n):
	sum = 0
	for i in range(1, n + 1):
		sum += i

	return sum == n * (n + 1) / 2

# "task1.check_equation(50)"
# 1000 loops, best of 3: 2.31 usec per loop

# "task1.check_equation(100)"
# 1000 loops, best of 3: 4.5 usec per loop

# "task1.check_equation(1000)"
# 1000 loops, best of 3: 60.5 usec per loop

# "task1.check_equation(10000)"
# 1000 loops, best of 3: 663 usec per loop

#  1    0.000    0.000    0.000    0.000 task1.py:6(check_equation)

def check_equation_easy_way(n):
	return sum(range(1, n + 1)) == n * (n + 1) / 2

# "task1.check_equation_easy_way(50)"
# 1000 loops, best of 3: 1.02 usec per loop

# "task1.check_equation_easy_way(100)"
# 1000 loops, best of 3: 1.38 usec per loop

# "task1.check_equation_easy_way(1000)"
# 1000 loops, best of 3: 17 usec per loop

# "task1.check_equation_easy_way(10000)"
# 1000 loops, best of 3: 190 usec per loop

# 1    0.000    0.000    0.000    0.000 task1.py:25(check_equation_easy_way)
