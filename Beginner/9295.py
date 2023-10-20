T = int(input()) # 테스트 케이스 수
lst = []
for i in range(T):
    num1, num2 = map(int, input().split())
    lst.append(f'Case {i+1}: {num1+num2}')
for i in lst:
    print(i)