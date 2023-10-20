'''import sys

max_name = ''
max_day = 0
max_month = 0
max_year = 0

min_name = ''
min_day = sys.maxsize
min_month = sys.maxsize
min_year = sys.maxsize
for _ in range(int(input())):
    name, day, month, year = input().split()
    day, month, year = map(int, [day, month, year])
    if min_year > year or min_year == year and min_month > month or min_year == year and min_month == month and min_day > day:
        min_name = name
        min_year = year
        min_month = month
        min_day = day
    if max_year < year or max_year == year and max_month < month or max_year == year and max_month == month and max_day < day:
        max_name = name
        max_year = year
        max_month = month
        max_day = day
print(max_name)
print(min_name)'''

# sort함수 활용
li = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    li.append([n, int(d), int(m), int(y)])
li.sort(key=lambda x:(x[3],x[2],x[1]))
print(li[-1][0])
print(li[0][0])