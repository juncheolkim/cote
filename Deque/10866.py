from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
answer = deque([])
for _ in range(N):
    string = input().split()
    if string[0] == "push_front":
        answer.appendleft(int(string[1]))
    elif string[0] == "push_back":
        answer.append(int(string[1]))
    elif string[0] == "pop_front":
        if answer:
            print(answer.popleft())
        else: print(-1)
    elif string[0] == "pop_back":
        if answer:
            print(answer.pop())
        else: print(-1)
    elif string[0] == "size":
        print(len(answer))
    elif string[0] == "empty":
        if answer:
            print(0)
        else: print(1)
    elif string[0] == "front":
        if answer:
            print(answer[0])
        else: print(-1)

    else:
        if answer:
            print(answer[-1])
        else: print(-1)