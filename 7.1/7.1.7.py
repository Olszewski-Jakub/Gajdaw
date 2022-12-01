h = int(input("Podaj h: "))

print(" " * ((2 * h - 1 - 1) // 2), end="")
print("X" , end="")
print(" " * ((2 * h - 1 - 1) // 2))
for x in range(3, 2*h-1, 2):
    a= 2 * h - 1 - x
    print(" "*(a//2),end="")
    print("X"*x,end="")
    print(" "*(a//2))
