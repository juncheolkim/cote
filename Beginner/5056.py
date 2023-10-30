t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    lst = [int(i) for i in input().split()]
    answer.append((max(lst) - min(lst)) * 2)
for i in answer:
    print(i)