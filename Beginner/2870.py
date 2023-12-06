N = int(input())
res = []
for _ in range(N):
    answer = ''
    content = input()
    for i in content:
        if i in '0123456789':
            answer += i
        else:
            if answer:
                res.append(int(answer))
                answer = ''
    if answer:
        res.append(int(answer))
res.sort()
for i in res:
    print(i)