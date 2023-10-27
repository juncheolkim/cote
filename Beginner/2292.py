N = int(input())

idx = 0
answer = 0
while N > 0:
    if idx == 0:
        N -= 1
    else:
        N -= idx * 6
    answer += 1
    idx += 1

print(answer)