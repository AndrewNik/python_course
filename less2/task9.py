number_count = int(input('Input count of numbers: '))

max_number, max_sum = 0, 0

for i in range(number_count):
	num = int(input(f'Input {i + 1} number: '))
	cur_sum = 0
	cur_num = num
	while cur_num > 0:
		cur_sum += cur_num % 10
		cur_num //= 10
	if cur_sum > max_sum:
		max_sum = cur_sum
		max_number = num

print(f'Max number: {max_number}. Sum of his digits: {max_sum}')