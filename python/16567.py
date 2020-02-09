'''
바이너리길은 N개의 0또는 1로 이루어진 수열
0 : 깨끗한 칸
1 : 더러운 칸
flip : 연속된 더러운 칸을 깨끗하게 만드는 기술
연속된 1을 0으로 만든다.

왕 : M개의 시련을 내린다.
"0" : 현재 길의 모든 칸을 깨끗하게 하기 위한 filp의 최소횟수를 하인들에게 외치게
"1 i" : 바이너리 길의 i번째 칸을 더럽힌다. 이미 더렵혀져 있다면 아무일도 일어나지 않는다.

입력 
첫째 줄에 칸의 개수 N / 시련의 개수 M
N개의 현재 바이너리 길의 상태가 주어진다.
M개의 줄에 시련이 주어진다

알고리즘

'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
road = list(map(int,input().split()))
flag, point,cnt = 0,set([]),0
for i in range(n):
    if road[i] == 1:
        point.add(i)
        if flag == 0:
            cnt += 1
            flag = 1
    else:
        flag = 0


for _ in range(m):
    com = input()
    if com[0] == "0":
        print(cnt)
    elif com[0] == "1":
        a,b = map(int,com.split())
        if b-1 not in  point :
            point.add(b-1)
            if b-1 == n-1 :
                if b-2 not in point:
                    cnt += 1
            elif b-1 == 0:
                if b not in point:
                    cnt += 1
            else:
                if b-2 in point  and b in point:
                    cnt -= 1
                elif b-2 not in point and b not in point:
                    cnt += 1


                    
            


