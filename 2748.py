'''
n = int(input())

def solution(a):
    if a == 1 :
        return 1
    elif a == 0 :
        return 0
    else:
        return solution(a-1) + solution(a-2)

print(solution(n))
'''
# 재귀로 푸니까 시간초과 -> 완전탐색으로 풀어볼까?
n = int(input())
if n == 0 :
    print(0)
elif n == 1 :
    print(1)
else:
    answer = [0,1]

    for i in range(2,90):
        answer.append(answer[i-2] + answer[i-1])

    print(answer[n])