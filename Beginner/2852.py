N = int(input())
cnt = 0
temp = ['0',0]
res = [0,0]
for _ in range(N):            
    team, time = input().split()
    M, S = map(int, time.split(':'))
    time = M*60 + S
    if team == '1':
        cnt -= 1
    else:
        cnt += 1
    if cnt < 0:
        if temp[0] == '0':
            temp[0] = '1'
            temp[1] = time
    if cnt > 0:
        if temp[0] == '0':
            temp[0] = '2'
            temp[1] = time
    if cnt == 0:
        if temp[0] != '0':
            if temp[0] == '1':
                res[0] += (time - temp[1])
            else:
                res[1] += (time - temp[1])
            temp[0] = '0'
            temp[1] = time
if cnt != 0:
    if temp[0] == '1':
        res[0] += (48*60 - temp[1])
    else:
        res[1] += (48*60 - temp[1])

for i in res:
    m,s = divmod(i,60)
    if m < 10:
        m = f'0{m}'
    if s < 10:
        s = f'0{s}'
    print(f'{m}:{s}')