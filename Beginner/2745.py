dic = {chr(x):i+10 for i, x in enumerate(range(65, 91))}
for i in range(10):
    dic[f'{i}'] = i
N, B = input().split()
B = int(B)
N = list(N)
N.reverse()

answer = 0
for i in range(len(N)):
    answer += (B**i) * int(dic[N[i]])     # 10 이상의 수
print(answer)