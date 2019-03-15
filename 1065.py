a = int(input())
if a < 100:
    print(a)
else:
    total = 99
    for i in range(100,a+1):
        list1 = [int(i) for i in str(i)]
        d = list1[0] - list1[1]
        ck = 0
        for j in range(1,3):
            if list1[j-1] - list1[j] != d:
                ck = 1
        if ck == 0:
            total += 1
    print(total)

    