lst = []
for _ in range(int(input())):
    c, v = map(int, input().split())
    a, b = divmod(c,v)
    lst.append(f'You get {a} piece(s) and your dad gets {b} piece(s).')
for i in lst:
    print(i)