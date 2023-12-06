N = int(input())
M = int(input())
lst = [int(i) for i in input().split()]
check = []
answer = 0
for i in lst:
    if i in check:
        check.remove(i)
        answer += 1
    else:
        check.append(M-i)

print(answer)