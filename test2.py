import sys
input = sys.stdin.readline

answer = [-1 for _ in range(10001)]
s,e = [0,0]

for _ in range(int(input())):
    lst_input = input().split()
    if lst_input[0] == 'push':
        answer[e] = int(lst_input[1])
        e += 1
    elif lst_input[0] == "pop":
        if s != e:
            print(answer[s])
            s += 1
        else: print(-1)
    elif lst_input[0] == "size":
        print(e - s)
    elif lst_input[0] == "empty":
        if s == e:
            print(1)
        else: print(0)
    elif lst_input[0] == "front":
        if s != e:
            print(answer[s])
        else: print(-1)
    else:
        if s != e:
            print(answer[e-1])
        else: print(-1)