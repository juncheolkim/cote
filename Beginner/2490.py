solution = {
    '0': 'D',
    '1': 'C',
    '2': 'B',
    '3': 'A',
    '4': 'E'
}
lst = []
for _ in range(3):
    lst.append(solution[str(sum(map(int,input().split())))])

for i in lst:
    print(i)