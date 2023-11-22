dp = [1,2,4,7]
for i in range(4,12):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    answer.append(dp[N-1])

for i in answer:
    print(i)