def suma_cyfr(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


n = int(input())
licznik = 0
suma = 0
x = 0
while licznik < n:
    if suma_cyfr(x) % 2 == 0:
        licznik += 1
        suma += x
    x += 1
print(suma)