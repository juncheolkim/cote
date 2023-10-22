
N = int(input())
answer = 0
for _ in range(N):
    isGroup = True
    checkGroup = []
    temp_str = ''
    # 주어진 단어
    string = input()
    # 'happy'
    for i in string:
        # 만약 그룹 단어가 아니면 반복 탈출
        if isGroup == False:
            break
        # 새로운 단어가 나오면 -> 체크그룹에 저장하고, temp_str 초기화
        if i != temp_str:
            checkGroup.append(temp_str)
            temp_str = i
        # 만약 체크그룹에 이미 존재하면 그룹단어 아니다
        if i in checkGroup:
            isGroup = False
    # 그룹단어라면 대답 + 1
    if isGroup == True:
        answer += 1
print(answer)