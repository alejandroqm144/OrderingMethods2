

import random
import time

numb = [random.randint(2, 58) for _ in range(8)]
print("Lista de números aleatorios: ")
print(numb)
print(" ")
time.sleep(2.5)

primes = []

powers = []

def es_primo(numb):
    if numb <= 1:
        return False
    elif numb <= 3:
        return True
    elif numb % 2 == 0 or numb % 3 == 0:
        return False
    i = 5
    while i * i <= numb:
        if numb % i == 0 or numb % (i + 2) == 0:
            return False
        i += 6
    return True

def siguiente_primo(numb):
    while True:
        numb += 1
        if es_primo(numb):
            return numb

for n in numb:
    if es_primo(n):
        primes.append(n)
    else:
        primes.append(siguiente_primo(n))

print("Lista de números primos: ")
print(primes)
print(" ")
time.sleep(2.5)

def elevar_a_n():
    for i in primes:
        n = random.randint(1, 3)
        power = i ** n
        powers.append(power)
    return powers

powers = elevar_a_n()

print("Lista de potencias primas: ")
print(powers)
print(" ")
time.sleep(2.5)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

sorted_powers = powers.copy()
radix_sort(sorted_powers)
print("Lista ordenada usando el método de Radix Sort:")
for i in range(len(sorted_powers)):
    print(sorted_powers[i], end=" ")
print(" ")
time.sleep(2.5)