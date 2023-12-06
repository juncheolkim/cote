res = []
while (t := input()) != '.' :
    tmp = []
    for i in t:
        if i in "[(":
            tmp.append(i)
        elif i == "]":
            if tmp and tmp[-1] == "[":
                tmp.pop()
            else:
                tmp.append(i)
        elif i == ")":
            if tmp and tmp[-1] == "(":
                tmp.pop()
            else:
                tmp.append(i)
    if tmp:
        res.append('no')
    else:
        res.append('yes')
for i in res:
    print(i)