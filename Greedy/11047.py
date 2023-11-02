N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.reverse()
answer = 0
idx = 0
while idx < N:
    if coins[idx] <= K :
        answer += K // coins[idx]
        K = K % coins[idx]
    else:
        idx += 1
print(answer)