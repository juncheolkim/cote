lst = [0,1]
for i in range(2,46):
    lst.append(lst[i-1]+lst[i-2])
print(lst[int(input())])