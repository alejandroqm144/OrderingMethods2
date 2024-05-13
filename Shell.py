

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

def shell_sort(arr):
    n = len(arr)
    brecha = n // 2
    while brecha > 0:
        for i in range(brecha, n):
            temp = arr[i]
            j = i
            while j >= brecha and arr[j - brecha] > temp:
                arr[j] = arr[j - brecha]
                j -= brecha
            arr[j] = temp
        brecha //= 2

    return arr

sorted_powers = shell_sort(powers)
print("Lista ordenada usando el método de Shell:")
for i in range(len(sorted_powers)):
    print(sorted_powers[i], end=" ")
print(" ")
time.sleep(2.5)