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

ch = set([(-2,+1),(-1,+2),(+1,+2),(+2,+1),(-2,-1),(-1,-2),(+1,-2),(+2,-1)])
for _ in range(int(input())):
    l = int(input())
    x,y = map(int,input().split())
    r_x,r_y = map(int,input().split())
    if x == r_x and y == r_y:
        print(0)
        continue
    stack = set([(x,y)])
    visited = [[0 for _ in range(l)] for _ in range(l)]
    cnt =0
    def find(visited,cnt,stack):
        while True:
            cnt += 1
            stack2 = set()
            for _ in range(len(stack)):
                t_x,t_y = stack.pop()
                for dx,dy in ch:
                    x_c = t_x + dx ; y_c = t_y + dy
                    if x_c>=0 and x_c<=l-1 and y_c>=0 and y_c<=l-1 and visited[y_c][x_c] == 0:
                        if x_c == r_x and y_c == r_y:
                            print(cnt)
                            return
                        visited[y_c][x_c] = 1
                        stack2.add((x_c,y_c))
            stack = stack2
    find(visited,cnt,stack)