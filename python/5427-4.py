# 빈 공간과 벽으로 이루어진 건물에 갇힘
# 건물의 일부에는 불이 났고,
# 상근이는 출구를 향해 뛰고 있다

# 매 초마다 불은 동서남북으로 펴져나간다
# 벽에는 불이 붙지 x
# 상근이는 동서남북 인접한 칸으로 이동할 수 있으며 1초가 걸림
# 상근이는 벽을 통과할 수 없고 
# 불이 붙거나 붙으려는 칸으로 이동x
# 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동 가능
# 얼마나 빨리 빌딩을 탈출할 수 있는지

#입력
# tc
# w,h
# h개줄의 w개의 문자
# . : 빈공간
# # : 벽
# @ : 시작위치
# * : 불

# 출력
# 가장빠른 시간 / 탈출할 수 없을 경우 IMPOSSIBLE
d_x = (1,-1,0,0)
d_y = (0,0,1,-1)
def find(stack,fire):
    while stack:
        # 불이 이동하고 사람이 따라옴
        # 사람이 있는 위치에 불이 올 수 있음
        # 불이 있는 위치로 사람은 갈 수 없음
        fire2 = set()
        for f_x,f_y in fire:
            for i in range(4):
                dx,dy = f_x+d_x[i], f_y+d_y[i]
                if dx<w and dx>=0 and dy<h and dy>=0 and matrix[dy][dx] != '#' and matrix[dy][dx] != '*':
                    matrix[dy][dx] = '*'
                    fire2.add((dx,dy))
        fire = fire2
        stack2 = set()
        for x,y,count in stack:
            for i in range(4):
                dx,dy = x+d_x[i], y+d_y[i]
                if dx<w and dx>=0 and dy<h and dy>=0 and matrix[dy][dx] != '#' and matrix[dy][dx] != '@' and matrix[dy][dx] != '*':
                    if dx == w-1 or dx == 0 or dy == h-1 or dy == 0:
                        return count+2
                    matrix[dy][dx] = '@'
                    stack2.add((dx,dy,count+1))
       
        stack = stack2
    return 0

for _ in range(int(input())):
    w,h = map(int,input().split())
    matrix = [[] for j in range(h)]
    fire = set()
    current = []
    for j in range(h):
        list1 = list(input())
        if '@' in list1:
            x ,y = list1.index('@'),j
        for k in range(w):
            if list1[k] == '*':
                fire.add((k,j))
        matrix[j] = list1
    if x == 0 or x == w-1 or y == 0 or y == h-1:
    # 처음에 바로 탈출하는 경우
        print(1)
    else:
        stack = set([(x,y,0)])
        ck = find(stack,fire)
        if ck == 0 :
            print("IMPOSSIBLE")
        else:
            print(ck)