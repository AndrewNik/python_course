# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

g = [
	[0, 0, 1, 1, 9, 0, 0, 0],
	[0, 0, 9, 4, 0, 0, 5, 0],
	[0, 9, 0, 0, 3, 0, 6, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 5, 0],
	[0, 0, 7, 0, 8, 1, 0, 0],
	[0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, st):
	length = len(graph)
	is_visited = [False] * length
	cost = [float('inf')] * length
	path_arr = [[]] * length
	parent = [-1] * length
	temp_st = st
	cost[st] = 0

	min_cost = 0

	while min_cost < float('inf'):
		is_visited[st] = True

		for i, vertex in enumerate(graph[st]):
			if vertex != 0 and not is_visited[i]:
				if cost[i] > vertex + cost[st]:
					cost[i] = vertex + cost[st]
					parent[i] = st

		min_cost = float('inf')
		for i in range(length):
			if min_cost > cost[i] and not is_visited[i]:
				min_cost = cost[i]
				st = i

	for idx, path in enumerate(path_arr):
		tmp_path = list()
		tmp_idx = idx
		if cost[idx] != float('inf'):
			if idx != temp_st:
				tmp_path.extend([temp_st, idx])
			else:
				tmp_path.append(temp_st)
		while parent[tmp_idx] != temp_st and parent[tmp_idx] != -1:
			tmp_path.insert(1, parent[tmp_idx])
			tmp_idx = parent[tmp_idx]
		path_arr[idx] = tmp_path.copy()

	return path_arr, cost


start = int(input('От какой вершины идти: '))
print('Список вершин обхода: {}, стоимость обхода: {}'.format(*dijkstra(g, start)))
