n = int(input())
licznik = 0
suma = 0
x = 0
while licznik < n:
    if x % 7 == 0:
        licznik += 1
        suma += x
    x += 1

print(suma)
