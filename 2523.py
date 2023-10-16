N = int(input())
for i in range(2*N-1):
    if i < N :
        print('*'*(1+i))
    else:
        print('*'*(2*N - i-1))