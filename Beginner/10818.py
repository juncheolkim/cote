N = int(input())
lst = [int(i) for i in input().split()]
max_value = -1000001
min_value = 1000001
for i in lst:
    if i < min_value : min_value = i
    if i > max_value : max_value = i
print(min_value,max_value)
