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


def find(m_pipe,n_use,use_num,index):
    global max_num
    if use_num > max_num:
        max_num = use_num
    if index == m:
        return
    for i in range(n):
        if n_use[i] == 0 and index < m and m_pipe[index] >= n_pipe[i] :
            m_pipe[index] -= n_pipe[i]
            n_use[i] = 1
            if index < m and m_pipe[index] < n_pipe[n-1]:
                find(m_pipe,n_use,use_num+1,index+1)    
            else:
                find(m_pipe,n_use,use_num+1,index)    
            m_pipe[index] += n_pipe[i]
            n_use[i] = 0

m = int(input())
m_pipe = list(map(int,input().split()))
m_pipe.sort(reverse=True)


n = int(input())
n_pipe = list(map(int,input().split()))
n_pipe.sort(reverse=True)

n_use = [0 for i in range(n)]

max_num = 0

if m_pipe[0] < n_pipe[0]:
    print(max_num)
else:
    index = 0
    find(m_pipe,n_use,max_num,index)
    print(max_num)


