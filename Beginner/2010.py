import sys
input = sys.stdin.readline
N = int(input())
answer = 0
for i in range(N):
    if i == 0:
        answer += int(input())
    else:
        answer += int(input()) - 1
print(answer)