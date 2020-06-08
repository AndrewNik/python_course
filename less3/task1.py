# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

multiple_list = [0 for _ in range(2, 10)]

for num in range(2, 100):
	for i in range(2, 10):
		if num % i == 0:
			multiple_list[i - 2] += 1

for idx, el in enumerate(multiple_list):
		print(f'{idx + 2} - {el}')