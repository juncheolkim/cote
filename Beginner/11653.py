N = int(input())

idx = 2
if (N!=1):
    while True:
        if (idx >= N):
            print(N)
            break
        p,r = divmod(N,idx)
        if r == 0:
            print(idx)
            N = p
        else:
            idx += 1
