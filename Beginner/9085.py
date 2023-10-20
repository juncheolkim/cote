lst = []
for i in range(int(input())):
    size = int(input())
    temp_lst = list(map(int,input().split()))
    lst.append(sum(temp_lst))
for i in lst:
    print(i)