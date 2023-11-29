import sys
sys.setrecursionlimit(10**7)

def dfs(y,x):
    if graph[y][x] == 0:
        visited[y][x] = 0
        return
    visited[y][x] = 1
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == -1 :
            dfs(ny,nx)
    return

res = []
dy = [1,1,1,-1,-1,-1,0,0]
dx = [0,1,-1,0,1,-1,1,-1]
while( T := input().split()):
    w, h = [ int(i) for i in T ]
    if w == 0 and h == 0 :
        break
    graph = []
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    for y in range(h):
        graph.append([int(i) for i in input().split()])
    answer = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x] == -1:
                if graph[y][x] == 0:
                    visited[y][x] = 0
                else:
                    dfs(y,x)
                    answer += 1
    res.append(answer)

for i in res:
    print(i)