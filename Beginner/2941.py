apl = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ipt = input()
idx = 0
answer = 0
while idx < len(ipt):
    if ipt[idx:idx+2] in apl:
        answer += 1
        idx += 2
    elif ipt[idx:idx+3] in apl:
        answer += 1
        idx += 3
    else:
        answer += 1
        idx += 1
print(answer)