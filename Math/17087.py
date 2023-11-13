import math
N, S = map(int, input().split())
lst = [abs(S - int(i)) for i in input().split()]
print(math.gcd(*lst))
