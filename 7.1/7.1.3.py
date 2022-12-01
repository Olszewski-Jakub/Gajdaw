h, l = map(int, input().split())
for x in range(l):
    print("X",end="")
print()
for x in range(h-2):
    print("X",end="")
    for y in range(l-2):
        print(" ",end="")
    print("X")
for x in range(l):
    print("X",end="")