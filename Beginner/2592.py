# 1000보다 작은 10의 배수 (1 ~ 100) * 10
lst_check = [0 for _ in range(101)]
answer = 0
for _ in range(10):
    n = int(input())
    lst_check[n//10] += 1
    answer += n

freq = lst_check.index(max(lst_check)) * 10
print(answer//10)
print(freq)