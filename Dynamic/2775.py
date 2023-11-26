T = int(input())
rooms = [[0 for _ in range(15)] for _ in range(15)]
for i in range(15):
    rooms[0][i] = i
for i in range(1,15):
    for j in range(1, 15):
        rooms[i][j] = sum(rooms[i-1][:j+1])

answer = []    
for _ in range(T):
    k = int(input())
    n = int(input())
    answer.append((k,n))

for k,n in answer:
    print(rooms[k][n])