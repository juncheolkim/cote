N = int(input())
K = int(input())
lst_pos = [int(i) for i in input().split()] # map, filter 사용 지양

lst_pos.sort()
lst_len = [lst_pos[i+1]-lst_pos[i] for i in range(N-1) if lst_pos[i+1] != lst_pos[i]]
lst_len.sort(reverse=True)
# 거리가 먼 부분 먼저 자른다.
# 내림차순으로 다 잘라버려
if K < len(lst_len):
    print(sum(lst_len[K-1:]))
else:
    print(0)