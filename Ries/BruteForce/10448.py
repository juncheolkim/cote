lst = [0,1]
for i in range(2,45):
    lst.append(i + lst[i-1])
answer = [0 for _ in range(1001)]
for i in range(1,len(lst)):
    for j in range(1,len(lst)):
        if lst[i]+lst[j] > 1000 :
            break
        for k in range(1,len(lst)):
            if lst[i]+lst[j]+lst[k] < 1001 :
                answer[lst[i]+lst[j]+lst[k]] = 1
            else : break
T = int(input())
answer_lst = []
for i in range(T):
    if answer[int(input())]:
        answer_lst.append(1)
    else: answer_lst.append(0)
for i in answer_lst:
    print(i)