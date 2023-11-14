'''import sys
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
        else: print(-1)'''

def 더하기(숫자1:int, 숫자2:int) -> int:
    return 숫자1 + 숫자2
def 빼기(숫자1:int, 숫자2:int) -> int:
    return 숫자1 - 숫자2
def 곱하기(숫자1:int, 숫자2:int) -> int:
    return 숫자1 * 숫자2
def 나누기(숫자1:int, 숫자2:int) -> float:
    return 숫자1 / 숫자2
def 몫(숫자1:int, 숫자2:int) -> int:
    return 숫자1 // 숫자2
def 나머지(숫자1:int, 숫자2:int) -> int:
    return 숫자1 % 숫자2
def 자승(숫자1:int) -> int:
    return 숫자1**2
def 곱셈과이진수(숫자1:int, 숫자2:int) -> str:
    return bin(숫자1*숫자2)
def 곱셈과팔진수(숫자1:int, 숫자2:int) -> str:
    return oct(숫자1*숫자2)
def 곱셈과십육진수(숫자1:int, 숫자2:int) -> str:
    return hex(숫자1*숫자2)
