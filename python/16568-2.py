n,a,b = map(int,input().split())
f,result,point = 0,0,[n]
diff,mini = max(a,b)+1,min(a,b)
up = n // (2*diff)
if up >= 1:
    result += 2*up-100
    point[0] -= (up*2*diff)-100*diff
    
while True :
    result += 1
    temp,f2 = [],0
    while point:
        cur = point.pop()
        cur -= 1
        if cur == 0 or cur-a == 0 or cur - b == 0:
            f = 1
            print(result)
            break
        if cur - a < 0 and cur - b < 0 :
            if cur >= mini:
                f2 = 1
            temp.append(cur)
        else:
            if cur-a > 0:
                if cur-a >= mini:
                    f2 = 1
                temp.append(cur-a)
            if cur-b >= 0 :
                if cur-b >= mini:
                    f2 = 1
                temp.append(cur-b)
    if f == 1:
        break
    if f2 == 0:
        print(result + min(temp))
        break
    point = list(set(temp))