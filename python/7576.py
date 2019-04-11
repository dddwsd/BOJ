# 격자모양에 토마토 하나 넣어서 보관
# 잘익은것 / 아직 익지 않은 것
# 보관 후 하루 -> 익은 토마토에 인접한 익지 않은 토마토는 익음
# 인접한 곳 -> 상하죄우
# 혼자 익는 경우 x
# 보관된 토마토들이 며칠이 지나야 다익는지 최소 일수

# 입력
# 상자의 크기
# 1 : 익은 토마토 0 : 익지않은 토마토 -1 : 토마토가 들어있지 않은 칸
# m: 가로 칸의 수 , n : 세로 칸의 수

# 출력
# 최소날짜 출력
# 저장될 때 모든 토마토 익어있으면 0
# 토마토가 모두 익지 못하는 상황이면 -1


m,n = map(int,input().split())
matrix = [0 for i in range(n)]
stack = set()

# j : x좌표 / i : y좌표
for i in range(n):
    list1 = []    
    list1 = list(map(int,input().split()))
    for j in range(m):
        if list1[j] == 1:
            stack.add((j,i,0))
    matrix[i] = list1

flag = 0
for i in range(n):
    if 0 in matrix[i]:
        flag = 1
if flag == 0:
    print(0)
else:   
    while stack:
        stack2 = set()
        length = len(stack)
        for x,y,count in stack:
            # 위
            if y+1 < n and matrix[y+1][x] == 0:
                matrix[y+1][x] = 1
                stack2.add((x,y+1,count+1))
            # 아래
            if y-1 >= 0 and matrix[y-1][x] == 0:
                matrix[y-1][x] = 1
                stack2.add((x,y-1,count+1))
            # 좌
            if x-1 >= 0 and matrix[y][x-1] == 0:
                matrix[y][x-1] = 1
                stack2.add((x-1,y,count+1))
            # 우
            if x+1 < m and matrix[y][x+1] == 0:
                matrix[y][x+1] = 1
                stack2.add((x+1,y,count+1))
        stack = stack2
        

    flag = 0
    for i in range(n):
            if 0 in matrix[i]:
                flag = 1
    if flag == 1:
        print(-1)
    else:
        print(count)    
        
        