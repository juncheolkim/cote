
sum = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += divmod(b,a)[1]
print(sum)