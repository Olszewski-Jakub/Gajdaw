n= int(input())
suma = 0
licznik = 0
x = 0
while licznik<n:
    if x % 2 == 0:
        suma += x
        licznik += 1
    x+=1

print(suma)