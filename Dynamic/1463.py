from collections import deque
X = int(input())
dequeue = deque([X])
visited = [0]*(X+1)
while dequeue:
    now = dequeue.popleft()
    if now == 1:
        break
    if now % 3 == 0 and visited[now//3] == 0:
        dequeue.append(now//3)
        visited[now//3] = visited[now] + 1
    if now % 2 == 0 and visited[now//2] == 0:
        dequeue.append(now//2)
        visited[now//2] = visited[now] + 1
    if now - 1 > 0 and visited[now-1] == 0:
        dequeue.append(now-1)
        visited[now-1] = visited[now] + 1
print(visited[1])