# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[int(input(f'Введите {col} элемент {row} строки: ')) for col in range(3)] for row in range(5)]

for row in matrix:
	row_sum = 0
	for col in row:
		row_sum += col
	row.append(row_sum)

print(matrix)
