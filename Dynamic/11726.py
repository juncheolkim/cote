lst = [1,2]
for i in range(2,1001):
    lst.append((lst[i-1]+lst[i-2])%10007)
print(lst[int(input())-1])