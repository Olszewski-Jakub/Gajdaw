h = int(input())

for x in range(h-1):
    print(" ",end="")
print("X")
for x in range(h-2):
    for y in range(h-x-2):
        print(" ",end='')
    print("X",end="")
    for y in range(2*x+1):
        print(" ",end="")
    print("X")
for x in range(2*h-1):
    print("X",end="")