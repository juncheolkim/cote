import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
def dfs(y,x):
    if graph[y][x] == 0:
        dp[y][x] = 0
        return
    dp[y][x] = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and dp[ny][nx] == -1:
            dfs(y+dy[i],x+dx[i])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = []
T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    answer = 0
    for y in range(N):
        for x in range(M):
            if dp[y][x] == -1:
                if graph[y][x] == 0:
                    dp[y][x] = 0
                else:
                    dfs(y,x)
                    answer += 1

    res.append(answer)

for i in res:
    print(i)