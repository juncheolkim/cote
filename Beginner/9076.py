T = int(input())
answer = []
for _ in range(T):
    lst = []
    ipt_lst = [int(i) for i in input().split()]
    ipt_lst.sort()
    if ipt_lst[-2] - ipt_lst[1] >= 4:
        answer.append("KIN")
    else:
        answer.append(sum(ipt_lst[1:-1]))
for i in answer:
    print(i)