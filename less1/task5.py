# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_index = int(input('Введите номер буквы в алфавите: '))
letter = chr(ord('a') + letter_index - 1)
print(f'На месте {letter_index} стоит буква "{letter}"')