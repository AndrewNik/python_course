# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def dfs(vert):
	is_visited[vert] = True
	for el in graph[vert]:
		if not is_visited[el]:
			dfs(el)


def gen_graph(num_vertex):
	graph = []
	for i in range(num_vertex):
		vertex = random.sample(range(num_vertex), random.randint(0, num_vertex))
		if i in vertex:
			vertex.remove(i)
		graph.append(vertex)
	return graph


num_v = int(input('Введите кол-во вершин графа: '))
graph = gen_graph(num_v)
print(f'Сгенерированный граф: {graph}')
start = int(input('С какой вершины начать? '))

is_visited = [False] * len(graph)
dfs(start)

