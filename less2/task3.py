# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число: '))
reverse = 0

while num > 0:
	reverse = reverse * 10 + num % 10
	num //= 10

print('Обратное по порядку цифр: ', reverse)
