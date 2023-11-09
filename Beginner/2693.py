N = int(input())

answer = []
for _ in range(N):
    lst_temp = [int(i) for i in input().split()]
    lst_temp.sort()
    answer.append(lst_temp[-3])
for i in answer:
    print(i)