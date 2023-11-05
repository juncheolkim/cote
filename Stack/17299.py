N = int(input())
ipt_lst = [int(i) for i in input().split()]
dic = {}
for i in ipt_lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

answer = [-1 for i in range(N)]
temp_stack = []
for i in range(N):
    idx = (N-i-1)
    ipt_temp = ipt_lst.pop()
    while temp_stack and temp_stack[-1][0] <= dic[ipt_temp]:
        if temp_stack[-1][0] == dic[ipt_temp]:
            temp_stack.pop()
            break
        else:
            temp_stack.pop()
    cnt = temp_stack[-1][1] if temp_stack else -1
    temp_stack.append((dic[ipt_temp],ipt_temp))
    answer[idx] = cnt

print(*answer)