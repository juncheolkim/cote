N = int(input())
lst = [0 for _ in range(1001)]
for i in range(2,1001):
    for m in range(2, 1000//i + 1):
        if i*m <= 1000:
            lst[i*m] += 1
lst[1] = 1
answer = 0
temp = list(map(int,input().split()))
for i in temp:
    if lst[i] == 0:
        answer+=1
print(answer)