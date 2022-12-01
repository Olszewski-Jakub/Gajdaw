h = int(input())

for x in range(h):
    for y in range(h):
        print(" ",end="")
    print("#")
for y in range(2*h+1):
    print("#", end="")
print()
for x in range(h):
    for y in range(h):
        print(" ",end="")
    print("#")