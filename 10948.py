import random

list = []
num = random.randrange(1,46)
list.append(num)
while len(list) < 6:
    if num in list:
        num = random.randrange(1,46)
        continue
    list.append(num)

print(list)


