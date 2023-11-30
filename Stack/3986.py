N = int(input())
answer = 0
for _ in range(N):
    string = list(input())
    tmp = []
    while string:
        cur = string.pop()
        if tmp and tmp[-1] == cur:
            tmp.pop()
        else:
            tmp.append(cur)
    if not tmp:
        answer += 1
print(answer)
