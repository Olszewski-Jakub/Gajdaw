n = int(input())
num = 1
for x in range(0, n):
    num = 1
    for y in range(0, x + 1):
        print(num, end=" ")
        num = num + 1
    print("\r")