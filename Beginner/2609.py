'''num1, num2 = map(int, input().split())

max_count = max(num1,num2)
min_count = min(num1, num2)
if min_count == 1 :
    print(1)
    print(max_count)
else:
    for i in range(min_count):
        temp = min_count - i
        if min_count % temp == 0 and max_count % temp == 0:
            print(temp)
            print(temp * max_count//temp * min_count//temp)
            break'''

# math 모듈 사용
import math
num1, num2 = map(int, input().split())
print(math.gcd(num1,num2))
print(math.lcm(num1,num2))