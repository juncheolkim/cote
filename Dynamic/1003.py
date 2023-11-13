def fibonacci(now: int,prev: int,lst_tmp: list,checked: list) :
    if now == 0 :
        checked[now] = True
        lst_tmp[prev][0] += 1
    elif now == 1 :
        checked[now] = True
        lst_tmp[prev][1] += 1
    elif checked[now]:
        lst_tmp[prev][0] += lst_tmp[now][0]
        lst_tmp[prev][1] += lst_tmp[now][1]
    else:
        fibonacci(now-1, now, lst_tmp, checked)
        fibonacci(now-2, now, lst_tmp, checked)
        checked[now] = True


T = int(input())
answer = []
for _ in range(T):
    lst_tmp = [[0,0] for _ in range(41)]
    checked = [False for _ in range(41)]
    N = int(input())
    if N == 0:
        answer.append([1,0])
    elif N == 1:
        answer.append([0,1])
    else:
        fibonacci(N-1,N,lst_tmp,checked)
        fibonacci(N-2,N,lst_tmp,checked)
        answer.append(lst_tmp[N])
    print(N,lst_tmp,checked)
print(answer)