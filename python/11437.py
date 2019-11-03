'''
N개의 정점으로 이루어진 트리
트리의 각 정점 : 번호가 매겨져 있다.
루트 : 1번
두 노드의 쌍 M개가 주어졌을 때 -> 가장 가까운 공통 조상이 몇번인지 출력
'''

'''
입력
첫째 줄 노드 N
N-1개 줄 : 트리상에서 연결된 두 정점
N번째 줄 : 가장 가까운 공통 조상을 알고 싶은 쌍의 개수 M
다음 M개 줄에는 정점 쌍이 주어진다
'''
from collections import deque
import sys
input = sys.stdin.readline

def find(x1,x2,parent,depth):
    # depth : x1 < x2로 설정 -> x2가 위로 올라와야함
    if depth[x1] != depth[x2]:
        if depth[x1] > depth[x2]:
            x1, x2 = x2, x1
        while True:
            # 
            flag = 0
            for i in range(20):
                if  depth[parent[x2][i]] < depth[x1]:
                    x2 = parent[x2][i-1]
                    break
                elif depth[parent[x2][i]] == depth[x1]:
                    x2 = parent[x2][i]
                    flag = 1
                    break
            if flag == 1:
                break
    print("x1 = ",x1," x2 = ",x2)
    if x1 != x2:
        for i in range(19,-1,-1):
            if parent[x2][i] != 0 and parent[x2][i] != parent[x1][i]:
                x1 = parent[x1][i]
                x2 = parent[x2][i]
        x2 = parent[x2][0]
    return x2


n = int(input())
adj = [[] for _ in range(n+1)]
parent = [[0] * 20 for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
depth[1],start = 1,deque()
for _ in range(n-1):
    x1 ,x2 = map(int,input().split())
    adj[x1].append(x2)
    adj[x2].append(x1)
start.append(1)
while start:
    cur = start.popleft()
    for item in adj[cur]:
        if depth[item] == 0:
            depth[item] = depth[cur] +1
            temp = cur
            k = 0
            while 2**k <= depth[item]:
                parent[item][k] = temp
                temp = parent[temp][k]
                k += 1
            start.append(item)

m = int(input())
result = []
for _ in range(m):
    x1 , x2 = map(int,input().split())
    result.append(str(find(x1,x2,parent,depth)))
print("\n".join(result))

    