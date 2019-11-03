'''
길이가 n인 수식
정수 : 0 ~ 9
연산자 : + - x
연산자의 우선순위는 모두 동일

괄호를 추가하면 괄호먼저
단 괄호 안에는 연산자가 하나만 들어있어야 한다.
괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하라
'''

'''
정수들 combination 2개
한줄로 만들고 마지막 계산 진행
'''

from itertools import combinations
from copy import deepcopy

cal = {'+': lambda x,y : x+y, '-':lambda x,y : x-y ,'*' : lambda x,y : x*y}

def cal_result(num,oper):
    t_num = deepcopy(num)
    t_oper = deepcopy(oper)
    n1 = t_num.pop(0)
    while t_num and t_oper:
        n2 = t_num.pop(0)
        op1 = t_oper.pop(0)
        n1 = cal[op1](n1,n2)
    return n1

def check(combi,n):
    temp = []
    
    while combi:
        index = [i for i in range(n)]
        t_list = combi.pop(0)
        flag = 0
        for item in t_list:
            if (item[0] in index) and (item[1] in index):
                index.remove(item[0])
                index.remove(item[1])
            else:
                flag = 1
        if flag == 0:
            temp.append(t_list)       
    return temp

def transform(num,oper,combi,val):
    for item in combi:
        t_num = deepcopy(num)
        t_oper = deepcopy(oper)
        item = sorted(item,key = lambda x : x[0],reverse = True)
        for list1 in item:
            n2 = t_num.pop(list1[1])
            n1 = t_num.pop(list1[0])
            op1 = t_oper.pop(list1[0])
            n1 = cal[op1](n1,n2)
            t_num.insert(list1[0],n1)
        val = max(val,cal_result(t_num,t_oper)) 
    return val

n = int(input())
line = input()
num = []
oper = []
for i in range(n):
    if i%2 == 0:
        num.append(int(line[i]))
    else:
        oper.append(line[i])

val = cal_result(num,oper)

index = []
for i in range(len(num)-1):
    index.append([i,i+1])
length = len(index)
combi = []
for i in range(1,length+1):
    combi.extend(list(combinations(index,i)))

combi = check(combi,len(num))
val = transform(num,oper,combi,val)
print(val)
