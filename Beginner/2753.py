u = int(input())
if u % 4 == 0 and u % 100 != 0 or u % 400 == 0:
    print(1)
else: print(0)