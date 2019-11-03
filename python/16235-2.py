d = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
def spring():
    global dic,matrix,a,n
    for key in dic.keys():
        x,y = map(int,key.split())
        total,temp,result,dead = matrix[y][x],dic[key],[],0
        while True:
            if temp[0] > total:
                for item in temp:
                    dead += item//2
                break
            else:
                age = temp.pop(0)
                total -= age
                result.append(age+1)
                if not temp:
                    break
        matrix[y][x] = total
        if result :
            dic[key] = result
        matrix[y][x] += dead
    for i in range(n):
        for j in range(n):
            matrix[i][j] += a[i][j]


def fall():
    global matrix,d,point,dic
    new_dic = {}
    for key in dic.keys():
        x,y = map(int,key.split())
        temp,total = dic[key],0
        for age in temp:
            if age % 5 == 0:
                total +=1
        if total > 0:
            for dx,dy in d:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    s_key = str(nx)+' '+str(ny)
                    if s_key not in new_dic:
                        new_dic[s_key] = []
                    plus = [1]*total
                    new_dic[s_key] += plus

    for key in new_dic.keys():
        if key in dic:
            dic[key] = new_dic[key]+dic[key]
        else:
            dic[key] = new_dic[key]

from pprint import pprint

n,m,k = map(int,input().split())
matrix,dic = [[5]*n for _ in range(n)],{}
a = [list(map(int,input().split())) for _ in range(n)]
point,result = [],0
for _ in range(m):
    temp = list(map(int,input().split()))
    temp[0],temp[1] = temp[1]-1,temp[0]-1
    key =str(temp[0])+" "+str(temp[1])
    if key not in dic:
        dic[key] = []
    dic[key].append(temp[2])

for key in dic.keys():
    dic[key].sort()

for _ in range(k):
    spring()
    fall()

for value in dic.values():
    result += len(value)
print(result)