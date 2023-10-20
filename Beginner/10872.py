'''
N = int(input())
def solution(n):
    if n == 0:
        return 1
    return n*solution(n-1)

print(solution(N))
'''
lst = [1]
for i in range(1,1000):
    lst.append(lst[i-1]*i)
print(lst[int(input())])
