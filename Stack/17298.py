N = int(input())
lst = [(i,int(v)) for i,v in enumerate(input().split())]
answer = [(i,-1) for i in range(N)]
temp = []
for i in lst:
    while temp and temp[-1][1] < i[1]:
        out = temp.pop()
        answer[out[0]] = i
    temp.append(i)

for i in answer:
    print(i[1],end=' ')