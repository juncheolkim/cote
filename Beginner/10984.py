lst = []
T = int(input())

for i in range(T):
    N = int(input()) # 과목의 수
    temp_c = 0
    temp_g = 0
    for m in range(N):
        C, G = map(float,input().split()) # 학점과 성적
        temp_c += int(C)
        temp_g += C * G
    lst.append([temp_c, round(temp_g/temp_c,1)])

for i in lst:
    print(*i)
