n, k = map(int, input().split())
if k == 1:
    print(n)
else:
    lst = []
    for i in range(1,k+1):
        temp = [j for j in str(n*i)]
        temp.reverse()
        lst.append(int(''.join(temp)))
    print(max(lst))