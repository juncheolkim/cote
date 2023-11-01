x = int(input())

idx = 0
while x > 0 :
    idx += 1
    x -= idx

if idx % 2 == 1:
    print(f'{1-x}/{idx+x}')
else:
    print(f'{idx+x}/{1-x}')