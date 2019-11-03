'''
캐슬 디펜스 : 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다.
게임이 진행되는 곳은 크기가 NxM인 격자판
각 칸에 포함된 적의 수는 최대 하나이다.

격자판의 N번행의 바로 아래(N+1)의 모든 칸에는 성이 있다.
성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다.
궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다.
각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다.

궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고,
그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.

같은 적이 여러 궁수에게 공격당할 수 있다.
공격받은 적은 게임에서 제외된다.
궁수의 공격이 끝나면 적이 이동한다.
적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다.
모든 적이 격자판에서 제외되면 게임이 끝난다.

게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져 있다.
따라서 이 게임의 궁수의 위치가 중요하다
격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.

격자판 (r1,c1) (r2,c2) 사이의 거리는
|r1-r2| + |c1-c2|

입력 N M D   -> D는 궁수의 공격 거리 제한
격자판 
0은 빈칸 
1은 적이있는칸
'''

'''
1. N+1행의 0~M-1까지 중에 궁수 3명
2. 궁수의 사거리 내의 적을 확인
3. 적이 확인되면 죽임 + 적 중복 가능 (가장 가까운 거리 + x좌표가 제일 작은 것)
4. 적은 시작부터 아래로 1씩 내려감
5. 모든 적이 사라지면 끝 
'''
from itertools import combinations
from copy import deepcopy

def simulation(dic,point,item,n,m,d,val):
    # item : 궁수 위치
    # point : 적위치 => y,x
    # dic :  m y x
    # kill : x,y,dist
    t_val = 0
    while True:
        kill = [[16,16,16],[16,16,16],[16,16,16]]
        for i in point:
            # 각 포인트 마다의 길이를 비교하여 좌표를 보관
            # 길이가 제일 짧고 x좌표가 제일 작은걸 한번 끝날때마다 out
            for j in range(3):
                if dic[item[j]][i[0]][i[1]] is not 0:
                    if dic[item[j]][i[0]][i[1]] < kill[j][2]:
                        kill[j][0],kill[j][1],kill[j][2] = i[1],i[0],dic[item[j]][i[0]][i[1]]
                    elif dic[item[j]][i[0]][i[1]] == kill[j][2]:
                        if i[1] < kill[j][0]:
                            kill[j][0],kill[j][1],kill[j][2] = i[1],i[0],dic[item[j]][i[0]][i[1]]
        # 지우기
        for i in kill:
            if i is not [16,16,16]:
                if [i[1],i[0]] in point:
                    point.remove([i[1],i[0]])
                    t_val += 1 
        # point없으면 끝
        if not point:
            return max(t_val,val)
        # 한칸 아래로
        for i in range(len(point)-1,-1,-1):
            if point[i][0]+1 == n:
                point.pop(i)
            else:
                point[i][0] += 1




def set_achor(dic,achor,matrix,n,m,d):
    for i in range(m):
        for j in range(n-1,-1,-1):
            for k in range(0,m):
                dist = abs(k-i) + abs(j-n)
                if dist <= d:
                    dic[i][j][k] = dist
    
n,m,d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
point = []
achor = [i for i in range(m)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            point.append([i,j])
dic = [[[0]*m for _ in range(n)]for _ in range(m)]
set_achor(dic,achor,matrix,n,m,d)
case = list(combinations(achor,3))
val = 0
for item in case:
    val = simulation(dic,deepcopy(point),item,n,m,d,val)
print(val)