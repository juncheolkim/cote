n, m = map(int,input().split())

def check_five(n:int):
    res = 0
    while n:
        n = n // 5
        res += n

    return res


def check_two(n:int):
    res = 0
    while n:
        n = n // 2
        res += n

    return res

n_ten = min(check_five(n),check_two(n))
n_and_m_ten = min(check_five(n-m)+check_five(m),check_two(n-m)+check_two(m))
print(n_ten - n_and_m_ten)