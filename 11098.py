lst = []
for _ in range(int(input())):
    temp = 0
    exp = ''
    for _ in range(int(input())):
        C, name = input().split()
        C = int(C)
        if temp < C :
            temp = C
            exp = name
    lst.append(exp)
for i in lst:
    print(i)