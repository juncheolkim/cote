all_lst = [input() for _ in range(5)]
length = max(list(map(len,all_lst)))
answer = ''
for i in range(length):
    for j in range(5):
        if i < len(all_lst[j]):
            answer += all_lst[j][i]
print(answer)