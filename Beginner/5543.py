bugurs = []
drinks = []
for i in range(5):
    price = int(input())
    if i in range(3):
        bugurs.append(price)
    else:
        drinks.append(price)
print(min(bugurs)+min(drinks)-50)