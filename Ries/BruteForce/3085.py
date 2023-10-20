N = int(input())
lst = [list(input()) for _ in range(N)]

def max_length(k,lst):
    lst_x = lst[k]
    length = len(lst_x)
    e = 0
    # 주어질 수 없는 키워드로 초기화
    color = 'K'
    max_size = 0
    temp_size = 0
    while e < length:
        if lst_x[e] != color:
            max_size = max(max_size,temp_size)
            color = lst_x[e]
            temp_size = 1
        else:
            temp_size+=1
        if e == length - 1:
            max_size = max(max_size,temp_size)
        e += 1
    e = 0
    color = 'K'
    temp_size = 0
    while e < length:
        if lst[e][k] != color:
            max_size = max(max_size,temp_size)
            color = lst[e][k]
            temp_size = 1
        else:
            temp_size+=1
        if e == length - 1:
            max_size = max(max_size,temp_size)
        e += 1
    
    return max_size

# 놓친 조건 : "상근이는 사탕의 색이 다른 인접한 두 칸을 고른다."
answer = 0
for y in range(N):
    for x in range(N):
        # 연속한 동일한 행의 두 값 바꾸기
        if x < N-1 and  lst[y][x] != lst[y][x+1]:
            # 파이썬에서 2차원 배열의 깊은 복사 방법
            temp_lst = [arr[:] for arr in lst]
            temp = temp_lst[y][x]
            temp_lst[y][x] = temp_lst[y][x+1]
            temp_lst[y][x+1] = temp
            for k in range(N):
                answer = max(answer, max_length(k,temp_lst))

        # 연속한 동일한 열의 두 값 바꾸기
        if y < N-1 and lst[y][x] != lst[y+1][x]:
            temp_lst = [arr[:] for arr in lst]
            temp = temp_lst[y][x]
            temp_lst[y][x] = temp_lst[y+1][x]
            temp_lst[y+1][x] = temp
            for k in range(N):
                answer = max(answer, max_length(k,temp_lst))

print(answer)