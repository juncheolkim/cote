max_people = 0
now = 0
for _ in range(10):
    o, i = [int(i) for i in input().split()]
    now += i - o
    max_people = max(max_people, now)
print(max_people)