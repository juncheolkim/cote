import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
store = [[] for _ in range(N+1)]

for i in range(N):
    time, pay = map(int,input().split())
    e = i + time
    if e <= N:
        store[e].append((time,pay))

res = 0
for i in range(1, N+1):
    if store[i]:
        for time, pay in store[i]:
            dp[i] = max(dp[i - time]+pay, res)
            res = dp[i]
    else:
        dp[i] = res

print(res)