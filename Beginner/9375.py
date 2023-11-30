T = int(input())
answer = []
for _ in range(T):
    dicFasion = {}
    n = int(input())
    if n == 0:
        answer.append(0)
        continue
    for _ in range(n):
        name, fasion = input().split()
        if fasion in dicFasion:
            dicFasion[fasion] += 1
        else:
            dicFasion[fasion] = 1
    res = 1
    for i in dicFasion:
        res *= (dicFasion[i] + 1)
    res -= 1
    answer.append(res)

for i in answer:
    print(i)
