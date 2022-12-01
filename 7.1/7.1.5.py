grubosc,wys,szer = map(int,input().split())
for x in range(wys-grubosc):
    for y in range(szer//2):
        print("L",end="")
    print()
for x in range(grubosc):
    for y in range(szer):
        print("L",end="")
    print()