from itertools import permutations

N = int(input())
throw = [list(map(int,input().split())) for _ in range(N)]
lst = list(permutations([1,2,3,4,5,6,7,8,9],3))
answer = 0
# print(lst)
for i in lst :
    temp_answer = 0
    for j in range(N):
        cnt = str(throw[j][0])
        s, b = [0,0]
        for k in range(3):
            if i[k] == int(cnt[k])  : s += 1
            elif str(i[k]) in cnt : b += 1
        if s == throw[j][1] and b == throw[j][2] :
            temp_answer += 1
    if temp_answer == N:
        answer += 1
print(answer)
