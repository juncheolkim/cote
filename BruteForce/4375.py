import sys
input = sys.stdin.readline

lst = '1'

while(n := input()):
    toInt = int(n)
    idx = 1
    while True:
        tmp = int(lst*idx)
        if tmp % toInt == 0:
            print(idx)
            break
        idx += 1