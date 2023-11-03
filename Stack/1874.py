n = int(input())
lst_answer = []
lst = [n-int(i) for i in range(n)]
lst_input = []

for _ in range(n):
    lst_input.append(int(input()))

lst_stack = []
idx = 0
while idx < n :
    if len(lst_stack) > 0 and lst_stack[-1] == lst_input[idx]:
        lst_stack.pop()
        lst_answer.append("-")
        idx += 1
    elif len(lst) == 0:
        lst_answer = ["NO"]
        break
    else:
        temp = lst.pop()
        lst_stack.append(temp)
        lst_answer.append("+")

for i in lst_answer:
    print(i)