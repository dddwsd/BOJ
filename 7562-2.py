# 체스판 위 나이트
# 나이트가 한 번에 이동할 수 있는칸
#  x  y
# -2 +1
# -1 +2
# +1 +2
# +2 +1
# -2 -1
# -1 -2
# +1 -2
# +2 -1
# 
# 나이트가 이동하려는 칸 주어짐
# tc
# 체스판 한변의 길이 l : 4 ~ 300 -> 체스판 크기 lxl
# 현재있는칸
# 이동하려는칸

for _ in range(int(input())):
    l = int(input())
    x,y = map(int,input().split())
    r_x,r_y = map(int,input().split())
    if x == r_x and y == r_y:
        print(0)
        continue
    stack = set([(x,y)])
    visited = [[0]*l for _ in range(l)]
    cnt =0
    def find(visited,cnt,stack):
        while True:
            cnt += 1
            stack2 = set()
            for t_x,t_y in stack:
                x_1 = t_x-2 ; y_1 = t_y+1
                x_2 = t_x-1 ; y_2 = t_y+2
                x_3 = t_x+1 ; y_3 = t_y+2
                x_4 = t_x+2 ; y_4 = t_y+1
                x_5 = t_x-2 ; y_5 = t_y-1
                x_6 = t_x-1 ; y_6 = t_y-2
                x_7 = t_x+1 ; y_7 = t_y-2
                x_8 = t_x+2 ; y_8 = t_y-1
                if x_1>=0 and x_1<=l-1 and y_1>=0 and y_1<=l-1 and visited[y_1][x_1] == 0:
                    if x_1 == r_x and y_1 == r_y:
                        print(cnt)
                        return
                    visited[y_1][x_1] = 1
                    stack2.add((x_1,y_1))
                if x_2>=0 and x_2<=l-1 and y_2>=0 and y_2<=l-1 and visited[y_2][x_2] == 0:
                    if x_2 == r_x and y_2 == r_y:
                        print(cnt)
                        return
                    visited[y_2][x_2] = 1
                    stack2.add((x_2,y_2))
                if x_3>=0 and x_3<=l-1 and y_3>=0 and y_3<=l-1 and visited[y_3][x_3] == 0:
                    if x_3 == r_x and y_3 == r_y:
                        print(cnt)
                        return
                    visited[y_3][x_3] = 1
                    stack2.add((x_3,y_3))
                if x_4>=0 and x_4<=l-1 and y_4>=0 and y_4<=l-1 and visited[y_4][x_4] == 0:
                    if x_4 == r_x and y_4 == r_y:
                        print(cnt)
                        return
                    visited[y_4][x_4] = 1
                    stack2.add((x_4,y_4))
                if x_5>=0 and x_5<=l-1 and y_5>=0 and y_5<=l-1 and visited[y_5][x_5] == 0:
                    if x_5 == r_x and y_5 == r_y:
                        print(cnt)
                        return
                    visited[y_5][x_5] = 1
                    stack2.add((x_5,y_5))
                if x_6>=0 and x_6<=l-1 and y_6>=0 and y_6<=l-1 and visited[y_6][x_6] == 0:
                    if x_6 == r_x and y_6 == r_y:
                        print(cnt)
                        return
                    visited[y_6][x_6] = 1
                    stack2.add((x_6,y_6))
                if x_7>=0 and x_7<=l-1 and y_7>=0 and y_7<=l-1 and visited[y_7][x_7] == 0:
                    if x_7 == r_x and y_7 == r_y:
                        print(cnt)
                        return
                    visited[y_7][x_7] = 1
                    stack2.add((x_7,y_7))
                if x_8>=0 and x_8<=l-1 and y_8>=0 and y_8<=l-1 and visited[y_8][x_8] == 0:
                    if x_8 == r_x and y_8 == r_y:
                        print(cnt)
                        return
                    visited[y_8][x_8] = 1
                    stack2.add((x_8,y_8))
            stack = stack2
    find(visited,cnt,stack)