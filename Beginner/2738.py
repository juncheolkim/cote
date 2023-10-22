N, M = map(int, input().split())

lst = [ [list(map(int, input().split())) for _ in range(N) ] for _ in range(2)]
answer = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        answer[i][j] = lst[0][i][j] + lst[1][i][j]
for i in answer:
    print(*i)