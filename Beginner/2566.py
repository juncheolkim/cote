max = -1
x,y = [-1,-1]

for i in range(9):
    lst = list(map(int, input().split()))
    for j in range(9):
        if lst[j] > max:
            max = lst[j]
            x, y = [i+1, j+1]
print(max)
print(x, y)