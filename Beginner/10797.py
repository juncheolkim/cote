n = int(input())
lst = list(map(int,input().split()))
print(len(list(filter(lambda x: x == n,lst))))