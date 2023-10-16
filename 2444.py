N = int(input())

for i in range(N):
    print(' '*(N-i-1)+'*'*(1+i*2))
N -= 1
for i in range(N):
    print(' '*(i+1)+'*'*(N*2-i*2-1))