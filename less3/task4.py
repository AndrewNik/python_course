# 4. Определить, какое число в массиве встречается чаще всего.

import random

list1 = [random.randint(1, 5) for _ in range(10)]
print(list1)

most_frq_el = list1[0]
max_frq = 1

for idx, el in enumerate(list1):
	frq = 1
	for nested_el in list1[idx + 1:]:
		if el == nested_el:
			frq += 1
	if frq > max_frq:
		max_frq = frq
		most_frq_el = el

print(f'Наиболее встречающийся элемент: {most_frq_el}, встретился {max_frq} раз.')