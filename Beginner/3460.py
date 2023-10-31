n = int(input())
lst = []
for _ in range(n):
    temp_lst = []
    temp = ''
    temp_cnt = int(input())
    idx = 0
    while temp_cnt // 2 != 0:
        temp_cnt, temp_push = divmod(temp_cnt, 2)
        if temp_push == 1:
            temp_lst.append(idx)
        idx += 1
    if temp_cnt :
        temp_lst.append(idx)
    lst.append(temp_lst)
for i in lst:
    print(*i)