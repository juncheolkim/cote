import sys
min = sys.maxsize
sum = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        sum += n
        if min > n :
            min = n
if min == sys.maxsize:
    print(-1)
else:
    print(sum)
    print(min)