N = int(input())
lst = []
for _ in range(N):
    d, w= map(int,input().split())
    lst.append([d,w])   # d: 마감일, w: 점수
lst.sort(key=lambda x : -x[0])  # 날짜 기준 정렬 (내림차순)
last_day = lst[0][0]
answer = 0
while last_day > 0:
    temp = [i[:] for i in lst if i[0] >= last_day]    # 마지막 마감일 기준으로 해결 할 수 있는 과제 선별
    if len(temp) == 0:  # 마감일 기준 해결할 과제 없으면 continue
        last_day -= 1
        continue
    temp.sort(key=lambda x: -x[1])   # 해결 할 수 있는 과제 중 가장 점수가 높은 과제를 뽑기 위해 정렬
    pop_item = temp[0]  # 가장 우선순위가 높은 과제
    answer += pop_item[1]
    lst.remove(pop_item)
    last_day -= 1
    
print(answer)

'''
5
4 50
100 40
100 40
100 40
1 30
'''