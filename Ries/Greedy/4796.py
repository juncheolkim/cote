lst = []
case_cnt = 0
while True:
    days = 0
    case_cnt += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0 :   #   탈출
        break
    days += V // P * L
    temp = V % P
    if temp :
        days += temp if temp < L else L
    lst.append([case_cnt, days])
for [case_, day_] in lst :
    print(f'Case {case_}: {day_}')