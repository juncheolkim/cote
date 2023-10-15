'''
import math

M = int(input())
N = int(input())
lst = []
for i in range(M,N+1):
    if (int(i**0.5)**2 == i) :
        lst.append(i)

if (len(lst) == 0) :
    print(-1)
else :
    print(sum(lst))
    print(lst[0])
'''
# 완전 탐색
M = int(input())
N = int(input())
sum = 0
min = 0

for i in range(1,101):
    if M <= i*i and N >= i*i :
        if sum == 0:
            min = i*i
        sum += i*i
if sum == 0 :
    print(-1)
else :
    print(sum)
    print(min)