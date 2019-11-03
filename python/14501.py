''''''
'''
N+1 되는날 퇴사할 예정
남은 N일 동안 최대한 많은 상담
하루에 1개씩 서로 다른 사람의 상담을 잡아놓았따
Ti : 상담을 완료하는데 걸리는 기간
Pi : 상담을 했을 때 받는 금액
최대수익 구하기
1. 상담이 가능한 날들을 찾는다.
2. 상담이 가능한 날들을 모두 시작점으로 잡는다

3. 시작점에서 이동하고 급여를 더한다
4. 이동 이후에 갈 수 있는 점들의 집합을 찾는다
5. 이동 이후에 갈 수 있는 점들을 시작점으로 정한다
6. 더이상 이동할 수 있는 점이 없을 때 급여를 현재까지 최대급여랑 비교하여 최대값을 정한다.
6. 3~6를 반복한다.
'''
def solution(start,val,result):
    temp = []
    for i in point:
        if i < start:
            break
        temp.append(i)
    if not temp:
        result[0] = max(val,result[0])
        return
    for item in temp:
        start += item-start + matrix[item][0]
        val += matrix[item][1]
        solution(start,val,result)
        start -= item-start + matrix[item][0]
        val -= matrix[item][1]

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
point,result = [],[0]
for i in range(n):
    if i+matrix[i][0] <= n:
        point.append(i)
point.sort(reverse=True)
solution(0,0,result)
print(result[0])