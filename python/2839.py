a = input()
b = int(a)//5
c = int(a)%5
total = b

if c == 1:
    if b >= 1:
        total -= 1
        total += 2
        print(int(total))
    else:
        print(-1)
elif c == 2:
    if b >= 2:
        total -= 2
        total += 4
        print(int(total))
    else :
        print(-1)
elif c == 3:
    total+=(c/3)
    print(int(total))
elif c == 4:
    if b >= 1:
        total -= 1
        total += 3
        print(int(total))
    else :
        print(-1)
elif c == 0:
    print(int(total))
    


#3 6 9 12 15 
#3 1 4  2  0  
