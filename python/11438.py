from collections import deque
from math import log2
import sys
input = sys.stdin.readline

def find(x1,x2,parent,depth):
    if depth[x1] > depth[x2]:
        x1, x2 = x2, x1
    gap = depth[x2] - depth[x1]
    i = 0
    while gap != 0:
        if gap%2 :
            x2 = parent[i][x2]
        gap //= 2
        i += 1
    if x1 != x2:
        for i in range(int(log2(n)),-1,-1):
            if parent[i][x2] != 0 and parent[i][x1] != parent[i][x2]:
                x1 = parent[i][x1]
                x2 = parent[i][x2]
        x2 = parent[0][x2]
    return x2

n = int(input())
adj = [[] for _ in range(n+1)]
parent = [[0]*(n+1) for i in range(int(log2(n))+1)]
# i th col : 하나의 노드에 대해 i의 2^log2n까지의 조상 저장
# i th row : 2^i번째 조상의 모흠
depth = [0 for _ in range(n+1)]
depth[1],start = 1,deque([1])
for _ in range(n-1):
    x1 ,x2 = map(int,input().split())
    adj[x1].append(x2)
    adj[x2].append(x1)

while start:
    cur = start.popleft()
    for item in adj[cur]:
        if depth[item] == 0:
            depth[item] = depth[cur] +1
            parent[0][item] = cur
            start.append(item)

for i in range(int(log2(n))):
    for j in range(1,n+1):
        parent[i+1][j] = parent[i][parent[i][j]]

m = int(input())
result = []
for _ in range(m):
    x1 , x2 = map(int,input().split())
    if x1 == 1 or x2 == 1:
        result.append(str(1))
    else:
        result.append(str(find(x1,x2,parent,depth)))
print("\n".join(result))

    