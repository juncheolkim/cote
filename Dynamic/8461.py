lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10,101):
    lst.append(lst[i-2]+lst[i-3])
T = int(input())
answer = []
for _ in range(T):
    answer.append(lst[int(input()) - 1])
for i in answer:
    print(i)