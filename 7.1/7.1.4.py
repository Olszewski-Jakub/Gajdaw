h = int(input())
for x in range(h, 1, -1):
    print(".", end="")
print("A")
space = 1
for line in range(2, h // 2 + 1):
    for x in range(h, line, -1):
        print(".", end="")
    print("A", end="")
    for x in range(space):
        print(".", end="")
    print("A")
    space += 2

for x in range(h, h // 2 + 1, -1):
    print(".", end="")

for x in range(space + 2):
    print("A", end="")
print()

