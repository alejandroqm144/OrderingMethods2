

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

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

sorted_powers = powers.copy()
heap_sort(sorted_powers)
print("Lista ordenada usando el método de Heap Sort:")
for i in range(len(sorted_powers)):
    print(sorted_powers[i], end=" ")
print(" ")
time.sleep(2.5)