from collections import deque
N = int(input())
lst = [True for _ in range(N)]
child = [[] for _ in range(N)]
temp = [int(i) for i in input().split()]
for i in range(N):
    if temp[i] == -1:
        parent = i
        continue
    child[temp[i]].append(i)
remove = int(input())
if remove == parent:
    print(0)
else:
    q = deque([remove])
    child[temp[remove]].remove(remove)
    lst[remove] = False
    while q:
        cur = q.popleft()
        if child[cur] :
            lst_tmp = child[cur][:]
            child[cur] = []
            for i in lst_tmp:
                q.append(i)
                lst[i] = False
    answer = 0
    for i,v in enumerate(lst):
        if v:
            if not child[i]:
                answer += 1
    print(answer)