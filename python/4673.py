all_list = [1 for _ in range(10001)]
for i in range(1,10001):
    ck = i + sum([int(j) for j in str(i)])
    if ck <= 10000:
        if all_list[ck] == 1:
            all_list[ck] = 0

for i in range(1,10001):
    if all_list[i] == 1:
        print(i)
    