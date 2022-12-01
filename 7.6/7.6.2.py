def suma_cyfr(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

print(suma_cyfr(int(input())))