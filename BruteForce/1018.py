M, N = map(int, input().split())
input_lst = []
for i in range(M):
    input_lst.append(input())

min_change = 64
for y in range(M-8+1):
    for x in range(N-8+1):
        # white 부터 채워진 체스판과의 차이
        min_start_W = 0
        # black 부터 채워진 체스판과의 차이
        min_start_B = 0
        for i in range(y,y+8):
            for j in range(x,x+8):
                if (i + j) % 2 == 0:
                    if input_lst[i][j] == 'B':
                        min_start_W += 1
                    else :
                        min_start_B += 1
                else:
                    if input_lst[i][j] == 'W':
                        min_start_W += 1
                    else:
                        min_start_B += 1

        min_change = min(min_change, min_start_W,min_start_B)



print(min_change)