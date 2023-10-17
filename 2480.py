lst = [0 for _ in range(7)]

a, b, c = map(int,input().split())
lst[a] += 1
lst[b] += 1
lst[c] += 1

if 3 in lst :
    print(10000 + lst.index(3)*1000)
elif 2 in lst:
    print(1000+lst.index(2)*100)
else:
    lst.reverse()
    print((6-lst.index(1))*100)