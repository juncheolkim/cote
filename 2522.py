N = int(input())
for i in range(2*N-1):
    if i < N :
        print(' '*(N-i-1)+'*'*(1+i))
    else:
        print(' '*(i-N+1)+'*'*(2*N - i-1))