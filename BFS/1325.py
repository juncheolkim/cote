from collections import deque
import sys
input = sys.stdin.readline
        
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int,input().split())
    graph[B].append(A)

answer = []
for i in range(1,N+1):
    visited = [False]*(N+1)
    q = deque([i])
    visited[i] = True
    cnt = 1
    while q :
        cur = q.popleft()
        for j in graph[cur]:
            if visited[j] == False:
                visited[j] = True
                q.append(j)
                cnt += 1
    answer.append(cnt)

max_cnt = max(answer)
for i in range(N):
    if answer[i] == max_cnt:
        print(i+1,end=' ')
