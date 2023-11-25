T = int(input())
answer = []
for _ in range(T):
    n = int(input())
    lst1 = [int(cost) for cost in input().split()]
    lst2 = [int(cost) for cost in input().split()]
    
    for i in range(n):
        if i == 0:
            lst1[i] = lst1[i]
            lst2[i] = lst2[i]
        elif i == 1:
            lst1[i] = lst1[i] + lst2[i-1]
            lst2[i] = lst1[i-1] + lst2[i]
        else:
            lst1[i] = max(lst2[i-1], lst2[i-2]) + lst1[i]
            lst2[i] = max(lst1[i-1], lst1[i-2]) + lst2[i]
    
    answer.append(max(lst1+lst2))
for i in answer:
    print(i)