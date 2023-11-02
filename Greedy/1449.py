N, L = map(int,input().split()) # N : 물이 새는 곳의 개수 N, L : 테이프의 길이
holes = list(map(int,input().split()))
holes.sort()
answer = 0
temp = 0
for hole in holes:
    if hole > temp :
        answer += 1
        temp = hole + L - 1
print(answer)