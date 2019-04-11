# switch 함수를 이용한 풀이

def switch(total,c):
    if c == 1:
        if total >= 1:
            total -= 1
            total += 2
            print(total)
        else:
            print(-1)
    elif c == 2:
        if total >= 2:
            total -= 2
            total += 4
            print(int(total))
        else :
            print(-1)
    elif c == 3:
        total+=(c/3)
        print(int(total))
    elif c == 4:
        if total >= 1:
            total -= 1
            total += 3
            print(int(total))
        else :
            print(-1)
    elif c == 0:
        print(int(total))


a = int(input())
b = a//5
c = a%5
total = b
switch(total,c)        




# 3 6 9 12 15
# 3 1 4  2  0
