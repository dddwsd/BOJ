'''
축구 평일 오후 / 의무 참석 x
N명이고 짝수이다
N/2로 스타트팀과 링크팀을 나눈다
사람에게 번호를 1 ~ N까지 배정 + 능력치 조사
S[i][j] = i번사람과 j번 사람이 같은 팀에 속했을때 더해지는 능력치
팀의 능력치는 팀에 속한 모든쌍의 능력치 S[i][j]의 합
S[i][j] 와 S[j][i] 는 다를 수 있으며
i와 j가 팀일 때 팀에 더해지는 능력치는 S[i][j] + S[j][i]이다.

두 팀의 능력치 최소화
'''
from itertools import combinations,permutations

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
list1 = []
for i in range(n):
    list1.append(i)

total = list(combinations(list1,int(n/2)))
total2 = []
length = int(len(total)/2)
for i in range(length):
    total2.append(total.pop())
gap = 100 * 20 * 20

for i in range(length):
    list1 = total.pop() ; list2 = total2.pop()
    temp1 = list(combinations(list1,2))
    temp2 = list(combinations(list2,2))
    max1 = 0 ; max2 = 0
    for i,j in temp1:
        max1 += matrix[i][j] + matrix[j][i]
    for i,j in temp2:
        max2 += matrix[i][j] + matrix[j][i]
    gap = min(abs(max1-max2),gap)
print(gap)




