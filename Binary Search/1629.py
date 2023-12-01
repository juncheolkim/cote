A, B, C = map(int, input().split())
# ( A ** B ) % C 출력
# ( A * B ) % C = (( A % C ) * ( B % C )) % C
# ( A ** B ) % C = (( A ** B//2 % C ) * ( A ** (B//2 + B%2))) % C = ...

dp = {}
def mod(a,b,c):
    if b in dp:
        return dp[b]
    if b == 1:
        return a%c
    if b == 0:
        return 1%c
    res = mod(a,b//2,c) * mod(a,b//2+b%2,c) % c
    dp[b] = res
    return res

print(mod(A,B,C))