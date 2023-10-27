from itertools import combinations
N , M = map(int, input().split())
lst = [sum(i) for i in combinations([int(i) for i in input().split()],3)]
lst.sort(reverse=True)
for i in lst:
    if i <= M:
        print(i)
        break