# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

letter1 = input('Введите 1 букву: ')
letter2 = input('Введите 2 букву: ')

index1 = ord(letter1.lower()) - ord('a') + 1
index2 = ord(letter2.lower()) - ord('a') + 1
distance = abs(index2 - index1) - 1
print(f'Буква {letter1} на месте {index1}. Буква {letter2} на месте {index2}.\nМежду ними {distance} букв.')

