# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Это алгоритм на решете Эратосфена

def sieve(num_idx):
	sieve_list = list(range(num_idx ** 2 + 2)) # такой размер решета точно будет содержать нужное простое число
	sieve_list[1] = 0  # без этой строки итоговый список будет содержать единицу
	for i in sieve_list:
		if i > 1:
			for j in range(i + i, len(sieve_list), i):
				sieve_list[j] = 0
	sieve_list = list(set(sieve_list))
	sieve_list.remove(0)
	return sieve_list[num_idx - 1]

# "prime.sieve(10)"
# 1000 loops, best of 3: 22.9 usec per loop

# "prime.sieve(50)"
# 1000 loops, best of 3: 576 usec per loop

# "prime.sieve(100)"
# 1000 loops, best of 3: 2.3 msec per loop

# "prime.sieve(500)"
# 1000 loops, best of 3: 72.3 msec per loop


# Это алгоритм на просто на проверка делимости

def prime(num_idx):
	prime_list = [2]
	tmp_num = 3
	while num_idx > len(prime_list):
		for j in prime_list:
			if tmp_num % j == 0:
				break
		else:
			prime_list.append(tmp_num)
		tmp_num += 1
	return prime_list.pop()

# "prime.prime(10)"
# 1000 loops, best of 3: 8.66 usec per loop

# "prime.prime(50)"
# 1000 loops, best of 3: 111 usec per loop

# "prime.prime(100)"
# 1000 loops, best of 3: 380 usec per loop

# "prime.prime(500)"
# 1000 loops, best of 3: 8.05 msec per loop
