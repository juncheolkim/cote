N = int(input())
s, e = input().split('*')
answer = []
for _ in range(N):
    string = input()
    check1 = string.startswith(s)
    if not check1:
        answer.append("NE")
        continue
    string = string[len(s):]
    check2 = string.endswith(e)
    if not check2:
        answer.append("NE")
        continue
    answer.append("DA")
for i in answer:
    print(i)