N = [int(i) for i in list(input())]
N.sort(reverse=True)
for i in N:
    print(i, end='')
