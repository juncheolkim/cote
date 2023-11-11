T = int(input())
answer = []

for _ in range(T):
    add_all = 0
    min_ = 100
    lst = [int(i) for i in input().split()]
    for i in lst:
        if i % 2 == 0:
            add_all += i
            min_ = min(i,min_)
    answer.append([add_all, min_])
for i in answer:
    print(*i)