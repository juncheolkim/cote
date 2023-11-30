dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0 for _ in range(26)]
N = int(input())
for _ in range(N):
    s = input()
    answer[dic.index(s[0])] += 1
    
res = ''
for i,v in enumerate(answer):
    if v >= 5:
        res += dic[i]

if res:
    print(res)     
else:
    print('PREDAJA')