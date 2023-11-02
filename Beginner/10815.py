N = int(input())
lst_n = input().split()
dic = {}
for i in lst_n:
    dic[i] = 1
M = int(input())
lst_m = input().split()
answer = []
for i in lst_m:
    if i in dic:
        answer.append(1)
    else: answer.append(0)
print(*answer)