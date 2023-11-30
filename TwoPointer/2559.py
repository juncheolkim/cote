N, K = map(int, input().split())
lst = [int(i) for i in input().split()]
s = 0
e = K
cur = sum(lst[s:e])
sum_max = cur
while e < N:
    cur = cur - lst[s] + lst[e]
    s += 1
    e += 1
    sum_max = max(sum_max, cur)
print(sum_max)