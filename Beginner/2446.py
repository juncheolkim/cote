N = int(input())
lst = []
for i in range(2*N-1):
    if i == N:
        lst.pop()
    if i < N:
        lst.append(' '*i+'*'*(2*(N-i)-1))
        print(lst[-1])
    else:
        print(lst.pop())