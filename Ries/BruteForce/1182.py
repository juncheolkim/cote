from itertools import combinations
N, S = map(int, input().split())
lst = list(map(int,input().split()))
answer = 0
for i in range(1,N+1):
    tmp_lst = map(sum,combinations(lst,i))
    for j in tmp_lst:
        if j == S:
            answer+=1

print(answer)