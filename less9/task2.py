# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
	def walk(self, code, acc):
		self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
		self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
	def walk(self, code, acc):
		code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"


def huffman_encode(s):
	h = []
	for ch, freq in Counter(s).items():
		h.append((freq, len(h), Leaf(ch)))
	heapq.heapify(h)
	count = len(h)
	while len(h) > 1:
		freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
		freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
		heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
		count += 1
	code = {}  # инициализируем словарь кодов символов
	if h:
		[(_freq, _count, root)] = h
		root.walk(code, "")
	return code


s = input('Введите строку для кодирования: ')
code = huffman_encode(s)  # кодируем строку
encoded = "".join(code[ch] for ch in s)
for ch in sorted(code):
	print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код
print(encoded)  # выведем закодированную строку
