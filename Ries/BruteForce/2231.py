N = int(input())
answer = [0 for _ in range(1000001)]
for i in range(1, 1000001):
    total = i
    temp = str(i)
    for m in temp :
        total += int(m)
    if total < 1000001 and answer[total] == 0:
        answer[total] = i
print(answer[N])