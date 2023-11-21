N = int(input())
lst = [0] + [int(i) for i in input().split()]
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i] , dp[i - j] + lst[j])
print(dp[-1])