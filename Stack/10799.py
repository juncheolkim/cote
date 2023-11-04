inp = input()
stick = 0
temp = ''
answer = 0
for i in inp:
    if i == ')':
        if temp == '(':
            answer += stick
        else:
            answer += 1
            stick -= 1
    else:
        if temp == '(':
            stick += 1
    temp = i

print(answer)