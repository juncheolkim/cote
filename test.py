'''lst = [[0 for _ in range(3)] for _ in range(3) ]
print(lst)
lst[1][1] = 1
print(lst)

A = [[0]*3]*3
print(A)
A[1][1] = 1
print(A)
'''
# print([i for i in range(1)])
'''from collections import deque
a = deque([1,2,3])
a.append(1)
a.popleft()
print(a)'''
'''lst_plug_stack = [1,2]
lst_plug_stack = list(map(lambda x : x-1 if x > 0 else 101, lst_plug_stack))
lst_plug_stack = list(map(lambda x : x-1 if x > 0 else 101, lst_plug_stack))
print(lst_plug_stack)'''

# print(sum([[1,2],[2,3]]))
print([i for i in range(2,1)])