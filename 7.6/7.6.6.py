def czy_palindrom(n):
    return str(n) == str(n)[::-1]

a,b = map(int, input().split())
r = []
for x in range(a,b):
    if czy_palindrom(x):
        r.append(x)

print(r)
