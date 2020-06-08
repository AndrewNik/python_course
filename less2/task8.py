# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

number_count = int(input('Input count of numbers: '))
search_digit = int(input('Input what digit we search: '))

digit_count = 0

for i in range(number_count):
	num = int(input(f'Input {i + 1} number: '))
	while num > 0:
		digit = num % 10
		if digit == search_digit:
			digit_count += 1
		num //= 10

print('Count of searching digit is', digit_count)

# easy way
# for i in range(number_count):
# 	num = input(f'Input {i + 1} number: ')
# 	digit_count += num.count(str(search_digit))
#
# print('Count of searching digit is', digit_count)