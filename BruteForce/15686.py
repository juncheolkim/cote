from itertools import combinations
from copy import deepcopy
import sys

# 입력받기
N, M = map(int, input().split())
graph = []
chicken_map = []
home_map = []
for y in range(N):
    lst = [int(i) for i in input().split()]
    for x in range(N):
        if lst[x] == 2:
            chicken_map.append((y,x))
            lst[x] = 0
        elif lst[x] == 1:
            home_map.append((y,x))
            lst[x] = 0
    graph.append(lst)

checked_chicken_map = combinations(chicken_map, M)
answer = sys.maxsize
for chickens in checked_chicken_map:
    tmp_answer = 0
    for y,x in home_map:
        tmp = sys.maxsize
        for ny,nx in chickens:
            tmp = min(tmp, abs(y-ny)+abs(x-nx))
        tmp_answer += tmp
    answer = min(answer, tmp_answer)

print(answer)