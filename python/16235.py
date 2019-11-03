''''''
'''
NxM크기의 땅
(r,c) : 각각의 칸 (1,1)부터 시작
r : y좌표
c : x좌표

로봇 S2D2 : 양분을 조사해서 전송 -> 모든칸에 대해서 조사

가장 처음 양분은 모든 칸에 5만큼 들어있다

나무 재테크 : 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크
M개의 나무 구매

4계절을 보낸다
1. 봄
-> 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가한다.
-> 각각의 나무는 나무가 있는 1x1 크기의 칸에 있는 양분만 먹을 수 있다
-> 하나의 칸에 여러개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
-> 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽는다

2. 여름
-> 봄에 죽은 나무가 양분으로 변한다.
-> 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. (소수점 아래 버린다)

3. 가을
-> 나무가 번식
-> 번식하는 나무는 나이가 5의 배수, 인접한 8개 칸에 나이가 1인 나무가 생긴다.
-> 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다

4. 겨울
-> S2D@가 땅을 돌아다니면서 땅에 양분을 추가한다.
-> 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

k년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램

입력
1. n,m,k
2. a행렬 -> s2d2가 양분을 주는 칸과 양
3. tree행렬 -> 상도가 심은 나무의 정보 -> x,y,z(나무나이)

matrix : 양분확인
tree : 각위치의 나무 나이
point : 현재 나무가 위치하고 있는 좌표
'''
d = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
def spring():
    global tree,matrix,point
    out,length = [],len(point)
    for _ in range(length):
        x,y = point.pop(0)
        total,temp,result,dead = matrix[y][x],tree[y][x],[],[]
        while True:
            if temp[0] > total:
                dead.append([x,y,temp])
                break
            else:
                age = temp.pop(0)
                total -= age
                result.append(age+1)
                if not temp:
                    break
        matrix[y][x] = total
        tree[y][x] = result
        if not result :
            out.append((x,y))
        else:
            point.append((x,y))
        for item in dead:
            x, y, temp = item
            for age in temp:
                matrix[y][x] += age // 2

    for i in range(n):
        for j in range(n):
            matrix[i][j] += a[i][j]



def fall():
    global matrix,tree,d,point
    p_point = []
    for item in point:
        x,y = item
        temp,total = tree[y][x],0
        for age in temp:
            if age % 5 == 0:
                total +=1
        if total > 0:
            for dx,dy in d:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    plus = [1]*total
                    tree[ny][nx] = plus + tree[ny][nx]
                    p_point.append((nx,ny))
    point = list(set(point).union(set(p_point)))

from pprint import pprint

n,m,k = map(int,input().split())
matrix,tree = [[5]*n for _ in range(n)],[[[] for _ in range(n)] for _ in range(n)]
a = [list(map(int,input().split())) for _ in range(n)]
point,result = [],0
for _ in range(m):
    temp = list(map(int,input().split()))
    point.append((temp[1]-1,temp[0]-1))
    tree[temp[0]-1][temp[1]-1].append(temp[2])
for item in point:
    x,y = item
    tree[y][x].sort()

for _ in range(k):
    spring()
    fall()


for item in point:
    x,y = item
    result += len(tree[y][x])
print(result)
