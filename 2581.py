lst = [0 for _ in range(10001)]
for i in range(2,10001):
    for m in range(2, 10000//i + 1):
        if i*m <= 10000:
            lst[i*m] += 1
lst[1] = 1
min = -1
sum = 0
for i in range(int(input()), int(input())+1):
    if lst[i] == 0:
        if min == -1:
            min = i
        sum += i

if min != -1:
    print(sum)
print(min)
