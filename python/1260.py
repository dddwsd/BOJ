def DFS():
    v = result.pop()
    print(v,end=" ")
    if edge[v]:
        for i in edge[v]:
            if visited[i] == 0:    
                result.append(i)
                visited[i] = 1
                DFS()
    return        

def BFS():
    while result:
        v = result.pop(0)
        print(v,end=' ')
        if edge[v]:
            for i in edge[v]:
                if visited[i] == 0:
                    result.append(i)
                    visited[i] = 1
               
n, m, v = map(int,(input().split()))
edge = [ [] for i in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

result = [v]
visited = [0 for i in range(n+1)]
visited[v] = 1
DFS()
print()

result = [v]
visited = [0 for i in range(n+1)]
visited[v] = 1
BFS()

