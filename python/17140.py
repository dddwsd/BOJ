''''''
'''
A : 3x3

1초 마다 배열에 연산이 적용
R연산 : 행의 개수 >= 열의 개수 : 배열 A의 모든 행에 대해서 정렬 -> 행을 느림
C연산 : 행의 개수 < 열의 개수 : 배열 A의 모든 열에 대해서 정렬 -> 열을 늘림

1. 정렬을 하려면 각각의 수가 몇번 나왓는지 알아야 한다.
2. 수의 등장횟수 오름차순 / 등장횟수가 같다면 값의 오름차순
3. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다

ex)
[3,1,1] => 3이 1번 1이 2번 등장
정렬된 결과는 [3,1,1,2]가 된다

[3, 1, 1, 2]
이 배열에는 3이 1번, 1이 2번, 2가 1번
=> [2,1,3,1,1,2]

딕셔너리를 통한 각 포인트 마다의 횟수 저장
value를 기준으로 value가 같으면 key를 기준으로 sorting

정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 커질 수 있다.
R연산 : 행의 크기가 가장 큰 행을 기준으로 모든 행의 크기가 커지고,
C연산 : 열의 크기가 가장 큰 열을 기준으로 모든 열의 크기가 커진다.
행 또는 열의 크기가 커진 곳에는 0이 채워진다.

수를 정렬할 때 0은 무시해야 한다.
ex)
[3,2,0,0]을 정렬한 결과는 [3,2]를 정렬한 결과와 같다.

행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.

1. r,c,k
2. 3개의 줄에 배열 A에 들어있는 수가 주어진다 

A[r][c]에 들어있는 값이 k가 되기위한 연산의 최소 시간을 출력한다.
이 값이 100을 넘어가는 경우에는 -1을 출력한다
'''
def cal(length):
    global matrix
    m_len = 0
    for i in range(length):
        key = set([0]).union(set(matrix[i]))
        key.remove(0)
        result = []
        for keys in key:
            result.append([keys, matrix[i].count(keys)])
        result.sort(key = lambda x : (x[1],x[0]))
        temp = [0]*100
        len1 = min(100,len(result)*2)
        m_len = max(len1,m_len)
        for j in range(len1//2):
            temp[2*j],temp[2*j+1] = result[j][0],result[j][1]
        matrix[i] = temp
    return m_len

def solution():
    global matrix
    cnt, row, col = 0, 3, 3
    while cnt<=100:
        if row < col:
            matrix = [list(t) for t in zip(*matrix)]
            row = cal(col)
            matrix = [list(t) for t in zip(*matrix)]
        else:
            col = cal(row)
        cnt += 1
        if matrix[r][c] == k:
            print(cnt)
            return
    print(-1)

r,c,k = map(int,input().split())
r,c = r-1,c-1
matrix = [[0]*100 for _ in range(100)]
for i in range(3):
    matrix[i][0],matrix[i][1],matrix[i][2] = map(int,input().split())
if 3 >= c+1 and 3 >= r+1 and matrix[r][c] == k:
    print(0)
else:
    solution()
