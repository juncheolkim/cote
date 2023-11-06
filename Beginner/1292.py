lst = []
idx = 1
while len(lst) < 1001:
    lst.extend([idx for _ in range(idx)])
    idx += 1
s,e = map(int,input().split())
print(sum(lst[s-1:e]))