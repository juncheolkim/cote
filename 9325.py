lst = []

T = int(input())
for i in range(T):
    sum = 0
    s = int(input())
    n = int(input()) # 서로 다른 옵션의 개수
    sum += s
    for m in range(n):
        q, p = map(int, input().split()) # 옵션 개수, 옵션 가격
        sum += q * p
    lst.append(sum)

for i in lst:
    print(i)
    
