N, M = map(int, input().split())
lst = [int(i) for i in input().split()]
s,e = [0,0]
sum = 0
answer = 0
while s < N:
    if e >= N:
        s += 1
        e = s
        sum = 0
        break
    sum += lst[e]
    if sum == M:
        answer += 1
        s += 1
        e = s
        sum = 0
    elif sum > M:
        s += 1
        e = s
        sum = 0
    else:
        e += 1
print(answer)