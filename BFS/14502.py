from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
lst_two = []
for y in range(N):
    tmp = [int(i) for i in input().split()]
    graph.append(tmp)
    for x in range(M):
        if tmp[x] == 2:
            lst_two.append([y, x])

# 0인 값 3개 조합
lst_zero_combi = [ [[a//M,a%M], [b//M,b%M], [c//M,c%M]] for a,b,c in list(combinations(range(M*N),3)) if graph[a//M][a%M] == 0 and graph[b//M][b%M] == 0 and graph[c//M][c%M] == 0 ]

res = 0
for a,b,c in lst_zero_combi:
    graph_tmp = deepcopy(graph)
    graph_tmp[a[0]][a[1]] = 1
    graph_tmp[b[0]][b[1]] = 1
    graph_tmp[c[0]][c[1]] = 1
    q = deque(lst_two)
    # bfs 탐색
    while q:
        cur = q.popleft()
        for i in range(4):
            ny, nx = cur[0] + dy[i], cur[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < M and graph_tmp[ny][nx] == 0:
                graph_tmp[ny][nx] = 2
                q.append([ny,nx])
    cnt = 0
    for y in range(N):
        for x in range(M):
            if graph_tmp[y][x] == 0:
                cnt += 1
    if cnt:
        res = max(cnt, res)

print(res)