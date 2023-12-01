N = int(input())
A = [int(i) for i in input().split()]
dp = [1 for _ in range(N)]

for i,v in enumerate(A):
    for j in range(i+1,N):
        if v > A[j]:
            dp[j] = max(dp[j],dp[i]+1)
print(max(dp))