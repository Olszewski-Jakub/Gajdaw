n = int(input())
licznik = 0
suma = 0
x = 0
while licznik<n:
    if x % 100 in [31,62,17]:
        suma += x
        licznik +=1
    x+=1
print(suma)