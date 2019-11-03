import sys

sys.setrecursionlimit(100000000)

def input():
    return sys.stdin.readline()[:-1]


def tree(node):
    for e in adj[node]:
        if depth[e] == -1:
            depth[e] = depth[node]+1
            parent[e][0] = node
            tree(e)


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
parent = [[0 for _ in range(20)] for _ in range(N+1)]
depth = [-1 for _ in range(N+1)]
depth[1] = 0
tree(1)
for j in range(20):
    for i in range(1, N+1):
        if parent[i][j]:
            parent[i][j+1] = parent[parent[i][j]][j]

for i in range(1,N+1):
    print(i," = ",parent[i])
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    if depth[A] < depth[B]:
        A, B = B, A
    gap = depth[A]-depth[B]
    for i in range(20):
        if gap == 0:
            break
        if gap%2:
            A = parent[A][i]
        gap //= 2
    if A != B:
        for i in range(19, -1, -1):
            if parent[A][i] and parent[A][i] != parent[B][i]:
                A = parent[A][i]
                B = parent[B][i]
        A = parent[A][0]
    print(A)
