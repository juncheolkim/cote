from itertools import combinations_with_replacement
N = int(input())
lst = [i for i in range(N+1)]
print(sum(list(map(lambda x : sum(list(x)),combinations_with_replacement(lst,2)))))