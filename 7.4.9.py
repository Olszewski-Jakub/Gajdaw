def is_prime(n):
    if n <2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True

n = int(input())
licznik,suma,x = 0,0,0
while licznik < n:
    if is_prime(x):
        licznik+=1
        suma += x
    x+=1
print(suma)