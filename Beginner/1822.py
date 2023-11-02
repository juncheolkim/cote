n = input()
set_a = {int(i) for i in input().split()}
lst_b = {int(i) for i in input().split()}

set_answer = list(set_a.difference(lst_b))
len_answer = len(set_answer)
if len_answer:
    print(len_answer)
    print(*sorted(set_answer))
else: print(len_answer)
