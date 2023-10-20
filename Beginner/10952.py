lst = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    lst.append(a+b)

for i in lst:
    print(i)