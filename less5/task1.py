# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

fabric_cnt = int(input('Кол-во предприятий: '))

fabric = namedtuple('fabric', 'qr1 qr2 qr3 qr4')
fabric_dict = {}

for i in range(fabric_cnt):
	name = input(f'Введите название {i + 1} предприятия: ')
	profit_list = [int(input(f'Введите прибыль за {i_profit + 1} квартал: ')) for i_profit in range(4)]
	fabric_dict[name] = fabric._make(profit_list)

total_profit = sum((sum(profit) for profit in fabric_dict.values()))

avg_total_profit = total_profit / fabric_cnt

print(f'Средняя прибыль для всех предприятий {avg_total_profit}')

print('Предприятия, чья прибыль выше среднего: ')
for name, p_list in fabric_dict.items():
	if sum(p_list) > avg_total_profit:
		print(f'{name:<15} --- {sum(p_list):>5}')

print('Предприятия, чья прибыль ниже среднего: ')
for name, p_list in fabric_dict.items():
	if sum(p_list) < avg_total_profit:
		print(f'{name:<15} --- {sum(p_list)}')
