N,M = map(int,input().split())
dicName = {}
dicNumber = {}
answer = []
for i in range(1,N+1):
    name = input()
    dicName[name] = i
    dicNumber[str(i)] = name
for _ in range(M):
    q = input()
    if q in dicName:
        answer.append(dicName[q])
    else:
        answer.append(dicNumber[q])
for i in answer:
    print(i)