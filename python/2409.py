# 건물 만들기 위해서 짧은 길이의 강철 파이프 N개
# 공사 때 사용하고 남은 긴길이의 파이프 M개
# M개 먼저 사용 -> 추가 주문
# 최대한 적게 주문

# 입력 
# 첫줄 M 개의 긴 강철 파이프
# 다음 줄 파이프 길이
# N
# 만들고자 하는 파이프의 길이

# 출력 만들 수 있는 필요한 파이프의 최대 개수
import sys
sys.setrecursionlimit(10**9)
from copy import *


total = 0

def find():
    global max_num
    global total
    while stack:
        total += 1
        c_m_pipe,c_n_use,use_num,index = stack.pop()
        if use_num > max_num:
            max_num = use_num
        total_num = 0

        for i in range(index,m):
            total_num += max_pipe[i]
        if use_num + total_num < max_num:
            continue
        c_m_pipe = list(c_m_pipe)
        c_n_use = list(c_n_use)
       

        for i in range(n-1,-1,-1):
            if c_n_use[i] == 0 and index < m and c_m_pipe[index] >= n_pipe[i] :
                c_m_pipe[index] -= n_pipe[i]
                c_n_use[i] = 1
                if index < m and c_m_pipe[index] < n_pipe[n-1]:
                    stack.add((tuple(c_m_pipe),tuple(c_n_use),use_num+1,index+1))
                else:
                    stack.add((tuple(c_m_pipe),tuple(c_n_use),use_num+1,index))
                c_m_pipe[index] += n_pipe[i]
                c_n_use[i] = 0

m = int(input())
m_pipe = list(map(int,input().split()))
m_pipe.sort(reverse=True)
max_pipe = deepcopy(m_pipe)

n = int(input())
n_pipe = list(map(int,input().split()))
n_pipe.sort(reverse=True)

maximum = 0
for i in range(0,m):
    cnt = 0
    for j in range(n-1,-1,-1):
        if max_pipe[i] >= n_pipe[j]:
            max_pipe[i] -= n_pipe[j]
            cnt+=1
        else:
            max_pipe[i] = cnt
            break


n_use = [0 for i in range(n)]

max_num = 0

if m_pipe[0] < n_pipe[0]:
    print(max_num)
else:
    index = 0
    stack = set([(tuple(m_pipe),tuple(n_use),max_num,index)])
    find()
    print(max_num)



