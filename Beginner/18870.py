N = int(input())
lst = [int(i) for i in input().split()]
dic = {}
for i,v in enumerate(sorted(set(lst))):
    dic[v] = i
for i in lst:
    print(dic[i],end=' ')