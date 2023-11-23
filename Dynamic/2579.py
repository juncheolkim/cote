T = int(input())
lst = [0]
for _ in range(T):
    lst.append(int(input()))

dp = [0,lst[1]]
if T == 1:
    print(lst[1])
elif T == 2:
    print(lst[1]+lst[2])
elif T == 3:
    print(max(lst[1]+lst[3], lst[2]+lst[3]))
else:
    dp.append(lst[1]+lst[2])
    dp.append(max(lst[1]+lst[3], lst[2]+lst[3]))
    for i in range(4,T+1):
        dp.append(max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i]))
    print(dp[-1])
