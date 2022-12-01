h = int(input())
space = 0
print("X")
for x in range(1,h-1):
    print("X",end="")
    for y in range(space):
        print(" ",end="")
    print("X")
    space +=1
for x in range(h):
    print("X",end="")