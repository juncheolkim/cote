white_rec = [[0 for _ in range(100)] for _ in range(100)]

T = int(input())
for _ in range(T):
    y, x = map(int, input().split())
    for i in range(10):
        for j in range(10):
            white_rec[y+i][x+j] = 1

for i in range(100):
    white_rec[i] = len(list(filter(lambda x: x == 1, white_rec[i])))

print(sum(white_rec))