import heapq

N = int(input())
lst_lectures = []
for _ in range(N):
    S, T = map(int,input().split())
    lst_lectures.append([S,T])

lst_lectures.sort(key= lambda x : x[0])
lst_rooms = []
heapq.heappush(lst_rooms,0)
for s,e in lst_lectures:
    if s >= lst_rooms[0]:
        heapq.heappop(lst_rooms)
        heapq.heappush(lst_rooms,e)
    else:
        heapq.heappush(lst_rooms,e)

print(len(lst_rooms))

'''
반례 :
8
5 6
3 7
1 8
8 10
6 11
11 12
10 14
9 16

답 : 3
오답 : 5
'''