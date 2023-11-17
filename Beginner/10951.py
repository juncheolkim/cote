import sys
input = sys.stdin.readline

while string:=sys.stdin.readline():
    print(sum([int(i) for i in string.split()]))