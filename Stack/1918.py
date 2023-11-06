from collections import deque

special = ['(', '-', ')', '*', '/', '+']
string = list(input())
stack_alp = deque([])
stack_spe = []
answer = ''
v = 0

def checkSum(v, stack_alp: deque, stack_spe):
    if len(stack_spe) == 0:
        return ''
    if v >= stack_spe[-1][1]:
        temp = ''
        while stack_alp:
            temp += stack_alp.popleft()
        while stack_spe:
            temp += stack_spe.pop()[0]
        return temp
    return ''

for i in string:
    if i == '(':
        v -= 2
    elif i == ')':
        v += 2
    elif i in ["*", "/"]:
        answer += checkSum(v,stack_alp,stack_spe)
        stack_spe.append((i,v))
    elif i in ["+", "-"]:
        answer += checkSum(v,stack_alp,stack_spe)
        stack_spe.append((i,v+1))
    else:
        stack_alp.append(i)

answer += checkSum(5,stack_alp,stack_spe)
    
print(answer)