lst = []
now = 0
for _ in range(4):
    outH, inH = map(int,input().split())
    now = now + inH - outH
    lst.append(now)
print(max(lst))