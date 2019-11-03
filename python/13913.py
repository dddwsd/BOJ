'''
수빈 : N
동생 : K

수빈 : 걷기 or 순간이동
걷기 : N-1 or N+1
순간이동 : 2*N

수빈이가 동생을 찾을 수 있는 가장 빠른 시간
'''
'''
출력
1. 가장 빠른 시간
2. 이동해야 하는 경로
'''
def find(root,dist,path):
    while root:
        point = root.pop(0)
        if point == k:
            print(dist[point])
            t_path = [point]
            while point != n:
                point = path[point]
                t_path.append(point)
            t_path.reverse()
            print(' '.join(map(str,t_path)))
            return
        for dx in (point-1,point+1,point*2):
            if 0 <= dx <= 100000 and dist[dx] == 0:
                dist[dx] = dist[point] + 1
                path[dx] = point
                root.append(dx)

n,k = map(int,input().split())
root = [n]
dist = [0]*100001
path = [0]*100001
find(root,dist,path)

