K = int(input())
res = []
for _ in range(K):
    P, M = map(int,input().split())
    lst = [0 for _ in range(M+1)]
    answer = 0
    for _ in range(P):
        sit_number = int(input())
        if lst[sit_number]:
            answer += 1
        else:
            lst[sit_number] = 1
    res.append(answer)
for i in res:
    print(i)