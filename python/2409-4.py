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

'''
런타임 에러
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때
'''
import sys
sys.setrecursionlimit(10**9)
from copy import *
import timeit

total = 0

def find():
    global max_num
    global total
    while stack:
        
        c_m_pipe,c_n_use,use_num,index = stack.pop()
        if use_num > max_num:
            max_num = use_num

        # index ~ m-1 를 더한 값
        if index >= 1 and use_num + maximum_index[m-1]-maximum_index[index-1] < maximum:
            continue
        c_m_pipe = list(c_m_pipe)
        c_n_use = list(c_n_use)
       

        for i in range(n-1,-1,-1):
            total += 1
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
start = timeit.default_timer()
maximum_index = [0 for i in range(m)]
ck = n-1
for i in range(0,m):
    cnt = 0
    for j in range(ck,-1,-1):
        if max_pipe[i] >= n_pipe[j]:
            max_pipe[i] -= n_pipe[j]
            cnt+=1
        else:
            ck = j
            max_pipe[i] = cnt
            if i == 0:
                maximum_index[i] = cnt
            else:
                maximum_index[i] = maximum_index[i-1] + cnt
            break
maximum = sum(max_pipe)

n_use = [0 for i in range(n)]

max_num = 0

if m_pipe[0] < n_pipe[0]:
    print(max_num)
else:
    index = 0
    stack = set([(tuple(m_pipe),tuple(n_use),max_num,index)])
   
    find()
    end = timeit.default_timer()
    print(total)
    print(end-start)
    print(max_num)




