string = input()
answer = ''
temp = ''
for i in range(len(string)):
    if temp and temp[0] == '<':
        if string[i] == '>':
            temp += string[i]
            answer += temp
            temp = ''
        else: temp += string[i]
    else:
        if string[i] == ' ':
            temp = temp[::-1]
            temp += string[i]
            answer += temp
            temp = ''
        elif string[i] == '<':
            temp = temp[::-1]
            answer += temp
            temp = ''
            temp += string[i]
        else:
            temp += string[i]
    if i == len(string)-1:
        if string[i] != '>':
            temp = temp[::-1]
        answer += temp
print(answer)