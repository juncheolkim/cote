lst1 = [0 for _ in range(101)]
lst2 = []
for _ in range(9):
    temp = int(input())
    lst1[temp] += 1
    lst2.append(temp)
lst1.reverse()
answer = 100 - lst1.index(1)
print(answer)
print(lst2.index(answer)+1)