N = int(input())
top = 20000
stk = []
answer = 0
for _ in range(N):
    stk.append(int(input()))
while stk:
    temp = stk.pop()
    if temp < top:
        top = temp
    else:
        answer += temp - top + 1
        top = top - 1
print(answer)