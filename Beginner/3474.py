def check_number(n,check):
    cnt = 0
    while n := (n//check):
        cnt += n
    return cnt


T = int(input())
res = []
for _ in range(T):
    t = int(input())
    five = check_number(t,5)
    two = check_number(t,2)
    res.append(min(five,two))

for i in res:
    print(i)