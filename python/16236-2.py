n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            t_x,t_y = j,i

'''
거리가 같으면 위로
y축이 같으면 왼쪽으로

해결방법
거리를 해당 위치에서 부터 1씩 증가시킨 점들을 모아놓고
해당 점들중에 제일 위에 있으면서 오른쪽에 있는 점을 찾아서 이동 반복
list를 사용하여 넣은 다음 sort시켜서 앞에 있는 점으로 이동

거리마다 갈 수 있는 점들 move에 넣기
먹을 수 있는 먹이를 dest에 넣기
dest가 존재하면 move를 멈추고 반복문을 빠져나옴 & 거리를 늘림
dest가 존재하지 않으면 거리를 1씩 늘려가면서 해당 거리의 모든점들을 move에 넣기
move의 len만큼 반복문을 돌려서 모든 점들에서 갈 수 있는 곳을 체크
'''
dest =[[t_y,t_x,0]]
size = 2
eat = 0
dist = 0

def print_list(matrix):
    for i in range(n):
        print(matrix[i])
    print()

while dest:
    visited = [[0]*n for _ in range(n)]
    list1 = dest.pop()
    x,y = list1[1],list1[0]
    matrix[y][x] = 0
    visited[y][x] = 1
    move = [[y,x,0]]

    while move:
        len1 = len(move)    
        for i in range(len1):
            x,y,length = move[i][1],move[i][0],move[i][2]
            #상
            if y+1 < n and 0<= matrix[y+1][x] <=size and visited[y+1][x] == 0 :
                visited[y+1][x] = 1
                move += [[y+1,x,length+1]]
                if 0 < matrix[y+1][x] < size:
                    dest += [[y+1,x,length+1]]
            #하
            if y-1 >= 0 and 0<= matrix[y-1][x] <= size and visited[y-1][x] == 0:
                visited[y-1][x] = 1
                move += [[y-1,x,length+1]]
                if 0 < matrix[y-1][x] < size:
                    dest += [[y-1,x,length+1]]
            #좌
            if x-1 >= 0 and 0<= matrix[y][x-1] <= size and visited[y][x-1] ==0 :
                visited[y][x-1] = 1
                move += [[y,x-1,length+1]]
                if 0 < matrix[y][x-1] < size:
                    dest += [[y,x-1,length+1]]
            #우
            if x+1 < n and 0<= matrix[y][x+1] <= size and visited[y][x+1] == 0:
                visited[y][x+1] = 1
                move += [[y,x+1,length+1]]
                if 0 < matrix[y][x+1] < size:
                    dest += [[y,x+1,length+1]]
        for i in range(len1):
            del move[0]
        if dest:
            dest.sort()
            eat += 1
            if eat == size:
                size +=1
                eat = 0
            dist += dest[0][2]
            matrix[dest[0][0]][dest[0][1]] = 9 
            dest = [dest[0]]
            break
    if not dest:
        break
        
print(dist)
    
    

        
        

