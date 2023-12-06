string = input()
dic = {}
for i in string:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

check_odd = []
for i in dic:
    if dic[i] % 2 :
        check_odd.append(i)

if len(check_odd) > 1:
    print("I'm Sorry Hansoo")
else:
    answer = []
    odd = ''
    if check_odd:
        odd = check_odd.pop()
        dic[odd] -= 1
        
    for i in dic:
        answer.append(i*(dic[i]//2))
    answer.sort()
    answer = ''.join(answer)
    print(answer + odd + answer[::-1])