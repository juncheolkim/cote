from collections import deque

N, K = map(int,input().split())
lst = deque([i for i in range(1,N+1)])
answer = []
cnt = 1
while lst:
    temp = lst.popleft()
    if cnt == K:
        answer.append(temp)
        cnt = 1
    else:
        lst.append(temp)
        cnt += 1


print("<",end='')
print(*answer,end='')
print(">")
