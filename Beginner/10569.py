# (꼭짓점의 수) - (모서리의 수) + (면의 수) = 2
T = int(input())
lst = []
for _ in range(T):
    V, E = map(int,input().split())
    lst.append(2 - V + E)
for i in lst:
    print(i)