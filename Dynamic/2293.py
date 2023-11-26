n, k = map(int,input().split())
dp = [0]*(k+1)

pocket = []
for _ in range(n):
    pocket.append(int(input()))
pocket.sort()
for coin in pocket:
    if coin > k:
        break
    dp[coin] += 1
    for i in range(coin,k+1):
        dp[i] += dp[i - coin]
print(dp[-1])