H, W = map(int,input().split())
res = []
for _ in range(H):
    answer = []
    case_ = input()
    cnt = -1
    for i in case_:
        if i == '.':
            if cnt < 0:
                answer.append(-1)
            else:
                cnt+=1
                answer.append(cnt)
        else:
            cnt = 0
            answer.append(cnt)
    res.append(answer)
for i in res:
    print(*i)