from itertools import combinations

lst = list(map(list,combinations([int(input()) for _ in range(9)], 7)))
sum_lst = list(map(sum,lst))
answer = lst[sum_lst.index(100)]
answer.sort()
for i in answer:
    print(i)