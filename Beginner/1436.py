N = int(input())
idx = 0
cnt = 0
while idx < N:
    cnt += 1
    if '666' in f'{cnt}':
        idx += 1
print(cnt)