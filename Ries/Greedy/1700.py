N,K = map(int,input().split())
lst = list(map(int,input().split()))
lst_plug = []
lst_plug_stack = []
lst_stack = []  # 가중치
for i in range(K):
    temp = lst[i]
    if temp not in lst[i+1:]:
        lst_stack.append(101)
    else:
        lst_stack.append(lst[i+1:].index(temp))
answer = 0
for i in range(K):
    if len(lst_plug) < N and lst[i] not in lst_plug:   # 멀티탭 빈자리 있을 때
        lst_plug.append(lst[i])
        lst_plug_stack.append(lst_stack[i])
    elif lst[i] in lst_plug:    # 똑같은 플러그가 이미 꽂혀 있을 때
        #   lst_plug_stack은 갱신해줘야한다.
        lst_plug_stack[lst_plug.index(lst[i])] = lst_stack[i]
    else:   # 플러그를 빼야하는 시점 -> 가중치 계산하기 / 가중치가 높은 멀티탭 뽑기
        lst_plug[lst_plug_stack.index(max(lst_plug_stack))] = lst[i]
        lst_plug_stack[lst_plug_stack.index(max(lst_plug_stack))] = lst_stack[i]
        answer += 1
    lst_plug_stack = list(map(lambda x : x-1 if x > 0 else 101, lst_plug_stack))
print(answer)


'''
좋은 반례 ->
4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
정답: 4
'''