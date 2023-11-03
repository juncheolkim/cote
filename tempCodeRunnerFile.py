for _ in range(int(input())):
    lst_input = input().split()
    if lst_input[0] == 'push':
        answer.append(lst_input[1])
    elif lst_input[0] == "pop":
        if answer:
            print(answer.())
        else: print(-1)
    elif lst_input[0] == "size":
        print(len(answer))
    elif lst_input[0] == "empty":
        if answer:
            print(0)
        else: print(1)
    elif lst_input[0] == "front":
        if answer:
            print(answer[0])
        else: print(-1)
    else:
        if answer:
            print(answer[-1])
        else: print(-1)