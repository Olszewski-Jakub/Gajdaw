n = int(input())
licznik = 0
suma = 0
x = 0
while licznik < n:
    if x % 2 != 0 :
        suma += x
        licznik += 1
    x+=1
print(suma)
