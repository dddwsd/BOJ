'''
새집 : NxN 격자판 
각각의 칸 (r(행),c(열)) / 행과 열은 1부터 시작
각각의 칸 : 빈칸 or 벽(갈 수 없다)

파이프 2개의 연속된 칸을 차지하는 크기이다.
회전 : 3가지 방향 가능하다 →, ↘, ↓


가로 : (y,x) *(y,x+1) - type 0
확인할 구역 
→ : (y,x+2) 
↘ : (y,x+2) / (y+1,x+1) / (y+1,x+2)

세로 : (y,x) *(y+1,x) - type 1
확인할 구역
↓ : (y+2,x)
↘ : (y+2,x) / (y+1,x+1) / (y+2,x+1)

대각선 : (y,x) (y,x+1) (y+1,x) *(y+1,x+1) - type 2
확인할 구역
→ : (y+1,x+2)
↘ : (y+2,x+1)
↓ : (y+1,x+2) (y+2,x+1) (y+2,x+2)

시작 (1,1) (1,2)
'''
dic = {}
def move(matrix,x,y,b_type,result):
    if x == n-1 and y == n-1:
        result[0] += 1
        return
    else:
        val = result[0]
        if str(x)+str(y)+str(b_type) in dic.keys():
            result[0] += dic[str(x)+str(y)+str(b_type)]
            return
        elif b_type == 0:
            if x+1 < n and matrix[y][x+1] is 0 :
                move(matrix,x+1,y,0,result)
            if x+1 < n and y+1 < n and matrix[y][x+1] is 0 and matrix[y+1][x] is 0 and matrix[y+1][x+1] is 0:
                move(matrix,x+1,y+1,2,result)
        elif b_type == 1:
            if y+1 < n and matrix[y+1][x] is 0 :
                move(matrix,x,y+1,1,result)
            if x+1 < n and y+1 < n and matrix[y][x+1] is 0 and matrix[y+1][x] is 0 and matrix[y+1][x+1] is 0:
                move(matrix,x+1,y+1,2,result)
        elif b_type == 2:
            if x+1 < n and matrix[y][x+1] is 0:
                move(matrix,x+1,y,0,result)
            if y+1 < n and matrix[y+1][x] is 0:
                move(matrix,x,y+1,1,result)
            if x+1 < n and y+1 < n and matrix[y][x+1] is 0 and matrix[y+1][x] is 0 and matrix[y+1][x+1] is 0:
                move(matrix,x+1,y+1,2,result)
        dic[str(x)+str(y)+str(b_type)] = result[0] - val
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
result = [0]
move(matrix,1,0,0,result)
print(result[0])
