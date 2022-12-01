n = list(map(int, list(input())))
print(n)
z = True
for x in n:
    if x % 2 != 0:
        z = False
        break
print("Tak" if z else "Nie")
