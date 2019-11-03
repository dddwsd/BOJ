'''
(r,c) : r행 c열
구역 다섯개 -> 지정
각 구역은 다섯 선거구 중 하나에 포함되어야 한다.

선거구는 구역을 적어도 하나 포함해야 하고,
한 선거구에 포함되어 있는 구역은 모두 연결되어야 한다.

0<= y <= y1
'''

def cal(x1,y1,x2,y2,x3,y3,x4,y4):
    global n,matrix
    area = [0 for _ in range(5)]
    for i in range(n):
        temp = matrix[i]
        if 0 <= i < y1:
            # 1 : 0 ~ x1
            # 2 : x1+1 ~ n-1
            area[0] += sum(temp[0:x1+1])
            area[1] += sum(temp[x1+1:n])
        elif y4 < i < n:
            # 3 : 0 ~ x4-1
            # 4 : x4 ~ n-1
            area[2] += sum(temp[0:x4])
            area[3] += sum(temp[x4:n])
        else:
            if y1 <= i < y2:
                # 1 : 0 ~ x1 - 1 - (i-y1)
                # 5 : x1 - (i-y1)
                area[0] += sum(temp[:x1-(i-y1)])
                start = x1 - (i-y1)
            if y2 <= i <= y4:
                # 3 : 0 ~ x2 - 1 + (i-y2)
                # 5 : x2 + (i-y2)
                area[2] += sum(temp[:x2+(i-y2)])
                start = x2 + i - y2
            if y1 <= i <= y3:
                # 2 : x1 + 1 +(i-y1) ~ n-1
                # 5 : ~ x1 + i-y1
                area[1] += sum(temp[x1+1+i-y1:n])
                end = x1+i-y1 + 1
            if y3 < i <= y4:
                # 4 : x3 - (i-y3) + 1 ~ n-1
                # 5 : x3 - (i-y3)
                area[3] += sum(temp[x3-(i-y3)+1:n])
                end = x3 - (i-y3) + 1
            area[4] += sum(temp[start:end])
    val = max(area) - min(area)
    return val

def simulation(x1,y1):
    global matrix
    result = []
    for n1 in range(1,x+1):
        for n2 in range(1,n-x):
            if y + n1 + n2 < n :
                x2,y2 = x1 - n1 , y1 + n1
                x3,y3 = x1 + n2 , y1 + n2
                x4,y4 = x2 + n2 , y2 + n2
                ret = cal(x1,y1,x2,y2,x3,y3,x4,y4)
                result.append(ret)
    
    return result



n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
result = []
for y in range(n):
    for x in range(n):
        ret = simulation(x,y)
        if ret:
            result.append(min(ret))


print(min(result))



