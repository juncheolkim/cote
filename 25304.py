X = int(input())
sum = 0
for i in range(int(input())):
    a,b = map(int,input().split())
    sum += a*b

answer = 'Yes' if X == sum else 'No'
print(answer)