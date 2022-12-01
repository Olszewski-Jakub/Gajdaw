def suma_cyfr(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    if len(str(s)) > 1:
        return suma_cyfr(s)
    return s


n = int(input())

a = suma_cyfr(n)
print(a)
