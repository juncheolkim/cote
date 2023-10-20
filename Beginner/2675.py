T = int(input())
lst = ['' for _ in range(T)]
for i in range(T):
    R, S = input().split()
    for m in S:
        lst[i] += m*int(R)
for i in lst:
    print(i)