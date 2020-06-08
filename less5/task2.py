# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается
# в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче
# под запретом. Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque


def to_dec(hex_list):
	dec_val = 0
	for idx, value in enumerate(hex_list[::-1]):
		dec_val += letter_weight[value] * 16 ** idx if value.isalpha() else int(value) * 16 ** idx
	return dec_val


def to_hex(dec_num):
	result = deque()
	while dec_num > 0:
		dec_num, remain = divmod(dec_num, 16)
		if remain >= 10:
			for key, value in letter_weight.items():
				if value == remain:
					remain = key
		result.appendleft(remain)
	return list(result)


fst_num = list(input('Введите первое число: ').upper())
snd_num = list(input('Введите второе число: ').upper())

letter_weight = {key: value for key, value in zip('ABCDEF', range(10, 16))}

fst_dec_num, snd_dec_num = to_dec(fst_num), to_dec(snd_num)

print(f'Сумма: {to_hex(fst_dec_num + snd_dec_num)}, произведение: {to_hex(fst_dec_num * snd_dec_num)}')
