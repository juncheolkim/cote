N = int(input())
lst = list(map(int,input().split()))
plus = [0 for _ in range(101)]
sum = 0
for i in range(len(lst)):
    if lst[i] == 1:
        if i == 0 or plus[i-1] == 0:
            plus[i] = 1
        else:
            plus[i] = plus[i-1]+1
        sum+=plus[i]
print(sum)