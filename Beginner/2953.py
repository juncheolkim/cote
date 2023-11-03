winner = 0
score = 0
for i in range(1,6):
    temp_score = sum(map(int,input().split()))
    if score <  temp_score :
        winner = i
        score = temp_score
print(winner, score)