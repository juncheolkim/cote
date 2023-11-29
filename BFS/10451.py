T = int(input())
res = []
for _ in range(T):
    N = int(input())
    visited = [-1 for _ in range(N)]
    graph = [int(i) for i in input().split()]
    answer = 0
    for i in graph:
        if visited[i-1] == -1:
            q = [i-1]
            while q:
                cur = q.pop()
                if visited[cur] != -1:
                    break
                visited[cur] = 1
                q.append(graph[cur]-1)
            answer += 1
    res.append(answer)
for i in res:
    print(i)