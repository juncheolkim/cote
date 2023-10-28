lst_answer = []
for _ in range(int(input())):
    n , s = input().split()
    n = int(n)
    s = s[:n-1] + s[n:]
    lst_answer.append(s)
for i in lst_answer:
    print(i)