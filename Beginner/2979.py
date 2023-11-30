A, B, C = map(int, input().split())
time_set = [0 for _ in range(101)]
for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s,e):
        time_set[i] += 1

print(A * time_set.count(1) + B * time_set.count(2) * 2 + C * time_set.count(3) * 3)