# 변화 순서는 항상 돌리는 면 기준
# 기존의 색 저장(+) : 돌리는면 기준 왼 위 오른 아래
# 기존의 색 저장(-) : 돌리는면 기준 오른 아래 왼 위
# 변경한 색 저장 : 돌리는면 기준 위 오른 아래 왼에다가 저장

def change_it(list1,check):
    if check == 0:
        # 시계방향으로 회전
        temp = list1[:]
        list1[0:3] = temp[6::-3]
        list1[3:6] = temp[7:0:-3]
        list1[6:9] = temp[8:1:-3]
    else:
        # 반시계방향으로 회전
        temp = list1[:]
        list1[0:3] = temp[2:9:3]
        list1[3:6] = temp[1:8:3]
        list1[6:9] = temp[0:7:3]
    return list1


def change_U(): # complete
    global list_u
    if a[1] == '+':
        temp1 = list_l[2::-1]
        temp2 = list_b[2::-1]
        temp3 = list_r[2::-1]
        temp4 = list_f[2::-1]
        list_b[2::-1] = temp1
        list_r[2::-1] = temp2
        list_f[2::-1] = temp3
        list_l[2::-1] = temp4
        list_u = change_it(list_u,0)

    else:
        temp1 = list_r[2::-1]
        temp2 = list_f[2::-1]
        temp3 = list_l[2::-1]
        temp4 = list_b[2::-1]
        list_b[2::-1] = temp1
        list_r[2::-1] = temp2
        list_f[2::-1] = temp3
        list_l[2::-1] = temp4
        list_u = change_it(list_u,1)

def change_D(): # complete
    global list_d
    if a[1] == '+':
        temp1 = list_l[6:9]
        temp2 = list_f[6:9]
        temp3 = list_r[6:9]
        temp4 = list_b[6:9]
        list_f[6:9] = temp1
        list_r[6:9] = temp2
        list_b[6:9] = temp3
        list_l[6:9] = temp4
        list_d = change_it(list_d,0)
    else:
        temp1 = list_r[6:9]
        temp2 = list_b[6:9]
        temp3 = list_l[6:9]
        temp4 = list_f[6:9]
        list_f[6:9] = temp1
        list_r[6:9] = temp2
        list_b[6:9] = temp3
        list_l[6:9] = temp4
        list_d = change_it(list_d,1)

def change_F():
    global list_f
    if a[1] == '+':
        temp1 = list_l[8:1:-3]
        temp2 = list_u[6:9]
        temp3 = list_r[0:7:3]
        temp4 = list_d[2::-1]
        list_u[6:9] = temp1
        list_r[0:7:3] = temp2
        list_d[2::-1] = temp3
        list_l[8:1:-3] = temp4
        list_f = change_it(list_f,0)
    else:
        temp1 = list_r[0:7:3]
        temp2 = list_d[2::-1]
        temp3 = list_l[8:1:-3]
        temp4 = list_u[6:9]
        list_u[6:9] = temp1
        list_r[0:7:3] = temp2
        list_d[2::-1] = temp3
        list_l[8:1:-3] = temp4
        list_f = change_it(list_f,1)

def change_B():
    global list_b
    if a[1] == '+':
        temp1 = list_r[8:1:-3]
        temp2 = list_u[2::-1]
        temp3 = list_l[0:7:3]
        temp4 = list_d[6:9]
        list_u[2::-1] = temp1
        list_l[0:7:3] = temp2
        list_d[6:9] = temp3
        list_r[8:1:-3] = temp4
        list_b = change_it(list_b,0)
    else:
        temp1 = list_l[0:7:3]
        temp2 = list_d[6:9]
        temp3 = list_r[8:1:-3]
        temp4 = list_u[2::-1]
        list_u[2::-1] = temp1
        list_l[0:7:3] = temp2
        list_d[6:9] = temp3
        list_r[8:1:-3] = temp4
        list_b = change_it(list_b,1)

def change_L(): # complete
    global list_l
    if a[1] == '+':
        temp1 = list_b[8:1:-3]
        temp2 = list_u[0:7:3]
        temp3 = list_f[0:7:3]
        temp4 = list_d[0:7:3]
        list_u[0:7:3] = temp1
        list_f[0:7:3] = temp2
        list_d[0:7:3] = temp3
        list_b[8:1:-3] = temp4
        list_l = change_it(list_l,0)
    else:
        temp1 = list_f[0:7:3]
        temp2 = list_d[0:7:3]
        temp3 = list_b[8:1:-3]
        temp4 = list_u[0:7:3]
        list_u[0:7:3] = temp1
        list_f[0:7:3] = temp2
        list_d[0:7:3] = temp3
        list_b[8:1:-3] = temp4
        list_l = change_it(list_l,1)

def change_R():
    global list_r
    if a[1] == '+':
        temp1 = list_f[8:1:-3]
        temp2 = list_u[8:1:-3]
        temp3 = list_b[0:7:3]
        temp4 = list_d[8:1:-3]
        list_u[8:1:-3] = temp1
        list_b[0:7:3] = temp2
        list_d[8:1:-3] = temp3
        list_f[8:1:-3] = temp4
        list_r = change_it(list_r,0)
    else:
        temp1 = list_b[0:7:3]
        temp2 = list_d[8:1:-3]
        temp3 = list_f[8:1:-3]
        temp4 = list_u[8:1:-3]
        list_u[8:1:-3] = temp1
        list_b[0:7:3] = temp2
        list_d[8:1:-3] = temp3
        list_f[8:1:-3] = temp4
        list_r = change_it(list_r,1)

tc = int(input())
for i in range(0,tc):
    num = int(input())
    list1 = []
    list1 = input().split()
    # U : 윗 D : 아래 F : 앞 B : 뒤 L : 왼쪽 R : 오른
    # - : 반시계 + : 시계
    # 초기 상태 : U : 흰 / D : 노란 / F : 빨간 / B : 오렌지 / L : 초록 / R : 파란
    # 윗면의 색상을 출력
    # 첫번재 줄에는 뒷면과 접하는 칸
    # 두번째, 세번째 줄은 순서대로
    # 흰 : w / 노 : y / 빨 : r / 오 : o / 초 : g / 파 : b
    # 모든 면은 해당 면을 정면으로 했을 때 맨윗줄부터의 색을 저장함
    list_u = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
    list_d = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
    list_f = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    list_b = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
    list_l = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
    list_r = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    for a in list1:
        temp1=[] # 돌리는 면 기준으로 위쪽 변경후 색
        temp2=[] # 오른쪽 변경 후 색
        temp3=[] # 아래쪽 변경 후 색
        temp4=[] # 왼쪽 변경 후 색
        if a[0] == 'U':
            change_U()
        elif a[0] == 'D':
            change_D()
        elif a[0] == 'F':
            change_F()
        elif a[0] == 'B':
            change_B()
        elif a[0] == 'L':
            change_L()
        elif a[0] == 'R':
            change_R()


    for j in range(1,10):
        print(list_u[j-1], end='')
        if j%3 == 0:
            print()