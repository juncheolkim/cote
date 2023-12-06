from collections import deque

def check(lst):
    cnt = 0
    for i in lst:
        cnt += i.count(1)
    return cnt

Y, X = map(int,input().split())
graph = []
for _ in range(Y):
    graph.append([int(i) for i in input().split()])

cur = check(graph)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
while cur:
    visited = [[True]*X for _ in range(Y)]
    visited[0][0] = False
    graph[0][0] -= 1
    q = deque([[0,0]])
    prev = 0
    while q:
        y,x= q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < Y and 0 <= nx < X:
                if graph[ny][nx] <= 0 and visited[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = False
                    graph[ny][nx] -= 1
                elif graph[ny][nx] == 1:
                    prev += 1
                    visited[ny][nx] = False
                    graph[ny][nx] -= 1
    cur -= prev

print(-graph[0][0])
print(prev)
