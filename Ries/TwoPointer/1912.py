'''
# 부르트 포스 시간초과
n = int(input())
answer = [-1001 for _ in range(n)]
lst = list(map(int,input().split()))
for i in range(len(lst)):
    for m in range(i,len(lst)):
        total = sum(lst[i:m+1])
        if answer[i] < total:
            answer[i] = total
print(max(answer))
'''
# 투포인터
import sys
input = sys.stdin.readline
s, e = [0, 0]
n = int(input())
lst = list(map(int,input().split()))
max = -1001
temp = 0
while e < n: # end 포인터가 범위를 벗어나면 종료
    temp += lst[e]
    if max < temp: # 합이 최댓값 보다 크면 최댓값 갱신
        max = temp
    if temp <= 0: # 합이 음수면 새로 세팅
        s = e
        temp = 0
    e += 1 # end 포인트는 계속 증가
print(max)
