N, K = map(int, input().split())
answer = 0
idx = 0
for i in range(1,N+1):
    if N % i == 0:
        idx += 1
    if idx == K and answer == 0:
        answer = i
print(answer)