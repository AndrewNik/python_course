# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random

answer = random.randint(0, 100)
for i in range(11):
	user_answer = int(input('Input number: '))
	if user_answer == answer:
		print(f'You win')
		break
	elif user_answer > answer:
		print('Real answer less than input')
	else:
		print('Real answer over than input')
else:
	print('Answer was ', answer)
