N = int(input())
game_map = [ [int(i) for i in input().split() ] for _ in range(N) ]
visited = [[ 0 for _ in range(N)] for _ in range(N)]
visited[0][0] = 1
for y in range(N):
    for x in range(N):
        if y != N-1 or x != N-1 and visited[y][x]:
            if x + game_map[y][x] < N:
                visited[y][x+game_map[y][x]] += visited[y][x]
            if y + game_map[y][x] < N:
                visited[y+game_map[y][x]][x] += visited[y][x]

print(visited[-1][-1])