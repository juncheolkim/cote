N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort(key=lambda x : (x[1], x[0]))
answer = 0
temp = 0
for s, e in lst:
    if s >= temp :
        temp = e
        answer += 1
print(answer)