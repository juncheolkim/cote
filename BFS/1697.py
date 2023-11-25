from collections import deque
N, K = map(int,input().split())
lst = [None] * 100001

q = deque([N])
lst[N] = 0
while q:
    cur = q.popleft()
    if cur*2 < 100001 and (lst[cur*2] == None or lst[cur]+1 < lst[cur*2]):
        lst[cur*2] = lst[cur]+1
        q.append(cur*2)
    if cur + 1 < 100001 and (lst[cur+1] == None or lst[cur]+1 < lst[cur+1]):
        lst[cur+1] = lst[cur]+1
        q.append(cur+1)
    if cur > 0 and (lst[cur-1] == None or lst[cur]+1 < lst[cur-1]):
        lst[cur-1] = lst[cur]+1
        q.append(cur-1)
print(lst[K])