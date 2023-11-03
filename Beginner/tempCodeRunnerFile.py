lst = []

for i in range(8):
    n = int(input())
    lst.append((i+1,n))

lst.sort(key=lambda x:-x[1])
sorted_answer = sorted(lst[:5],key=lambda x : x[0])
answer_point = 0
answer_lst = []
for i,v in sorted_answer:
    answer_lst.append(i)
    answer_point += v
print(answer_point)
print(*answer_lst)