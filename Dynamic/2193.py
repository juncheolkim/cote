N = int(input())
dp = [1,1,2]
for i in range(3,91):
    dp.append(sum(dp[:i-1])+1)
    
print(dp[N-1])

