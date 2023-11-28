def dfs(y,x):
    if graph[y][x] == 0:
        dp[y][x] = 0
        return 0
    dp[y][x] = graph[y][x]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and dp[ny][nx] == -1:
            dp[y][x] += dfs(ny,nx)
    return dp[y][x]




N = int(input())
dp = [[-1 for _ in range(N)]for _ in range(N)]
graph = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for _ in range(N):
    graph.append([int(i) for i in input()])
answer = []
for y in range(N):
    for x in range(N):
        if dp[y][x] == -1:
            tmp = dfs(y,x)
            if tmp:
                answer.append(tmp)

answer.sort()
print(len(answer))
for i in answer:
    print(i)