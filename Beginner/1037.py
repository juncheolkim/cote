N = int(input())
s = set()
lst = [int(i) for i in input().split()]
lst_check = [0 for _ in range(1000001)]
if N == 1:
    print(lst[0]**2)
else:
    print(min(lst)*max(lst))