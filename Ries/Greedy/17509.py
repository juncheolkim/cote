answer = 0
T = 0
lst = [list(map(int,input().split())) for _ in range(11)]
lst.sort(key= lambda x: x[0])
for D,V in lst:
    T += D
    answer += T + 20 * V
print(answer)