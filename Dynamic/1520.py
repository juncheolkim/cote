import sys
input = sys.stdin.readline

def dfs(y,x):
    if dp[y][x] != -1:
        return dp[y][x]
    # 도착지점에 도착할 때마다 카운트
    cnt = 0
    for i in range(4):
        tmpY = y + posY[i]
        tmpX = x + posX[i]
        if M > tmpY >= 0 and N > tmpX >= 0 and graph[y][x] > graph[tmpY][tmpX]:
            cnt += dfs(tmpY, tmpX)
    # 만약 도달 가능한 경로가 없으면 0을 반환
    dp[y][x] = cnt
    return dp[y][x]

posX = [1, 0, -1, 0]
posY = [0, 1, 0, -1]
M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append([int(i) for i in input().split()])

# 순회하지 않은 경로인지, 가능성이 없는 경로인지 구분해야하기 때문에 -1로 초기화해야 한다.
dp = [[-1 for _ in range(N)] for _ in range(M)]
# 마지막 도달 위치는 1로 초기화
dp[-1][-1] = 1
answer = 0

print(dfs(0,0))