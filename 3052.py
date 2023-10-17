'''s = set()
for _ in range(10):
    s.add(int(input())%42)
print(len(s))'''

lst = [0 for _ in range(1001)]
for _ in range(10):
    lst[int(input())%42] += 1
a = list(filter(lambda x : x != 0, lst))
print(len(a))
