# 기본적으로 부모와 자식 사이를 1촌
# 나와 아버지 1촌 / 아버지 할아버지 1촌 / -> 나와 할아버지 2촌
# 아버지 형제들과 할아버지는 1촌 -> 나와 아버지 형제들은 3촌

# 입력
# 첫줄 : 사람의 수 = n
# 둘째줄 : 촌수를 계사해야 하는 두 사람의 번호
# 셋째줄 : 부모 자식들 간의 관계의 개수 m
# 넷째줄 부터 m개의 줄 : 부모 자식간의 관계를 나타내는 두번호 x,y (x부모 y자식)
# cf) 각 사람의 부모는 최대 한명

def find():        
    while result:
        count, matrix = result.pop()
        visited[matrix] = 0
        if visited[parent[matrix]] == 1:
            if parent[matrix] == r2:
                print(count+1)
                return 0
            result.add((count+1,parent[matrix]))
        if child[matrix] != 0 :
            for i in child[matrix]:
                if i == r2:
                    print(count+1)
                    return 0
                if visited[i] == 0:
                    pass
                result.add((count+1,i))
    return 1
        
n = int(input())
r1, r2 = map(int,input().split())
m = int(input())
dic = {}
visited = [0 for i in range(n+1)]
child = [0 for i in range(n+1)]
parent = [0 for i in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    visited[x] = 1
    visited[y] = 1
    parent[y] = x
    if child[x] == 0:
        child[x] = []
        child[x].append(y)
    else:
        child[x].append(y)
    


result = set([(0,r1)])

n = find()
if n == 1:
    print(-1)
