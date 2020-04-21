'''
배열 : 3 x 3

1초가 지날 때 마다 배열에 연산이 적용된다.

R 
- 배열 A의 모든 행에 대해 정렬을 수행
- 행의 개수 >= 열의 개수인 경우
C
- 배열 A의 모든 열에 대해 정렬을 수행
- 행의 개수 < 열의 개수인 경우

정렬 기준
1. 수의 등장 횟수가 커지는 순으로
2. 등장 횟수가 동일하면 수가 커지는 순으로
3. 배열에 넣을 때 : 수 + 등장 횟수

R 연산
- 행의 크기가 가장 큰 행을 기준으로 모든 행의 크기가 커진다.
C 연산
- 열의 크기가 가장 큰 열을 기준으로 모든 열의 크기가 커진다.

행 또는 열의 크기가 커진 곳에는 0이 채워진다.
수를 정렬할 때는 0은 무시한다.

행 or 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다

A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간
100을 넘어가는 경우 -1을 출력
'''
r,c,k = map(int,input().split())
r,c = r-1,c-1
matrix = [list(map(int,input().split())) for _ in range(3)]
result, row_len, col_len = -1, 3, 3

from pprint import pprint

def r_cal(matrix,row_len,col_len):
	max_len = 0 
	length = []
	for y in range(row_len):
		dic = {}
		temp = list(matrix[y])
		for x in range(col_len):
			if temp[x] == 0:
				continue
			if temp[x] not in dic:
				dic[temp[x]] = 0
			dic[temp[x]] += 1
		sort = sorted(list(map(list,dic.items())),key = lambda x : (x[1],x[0]))
		sort = sum(sort,[])
		length.append(len(sort))
		max_len = max(max_len,len(sort))
		matrix[y] = sort
	for y in range(row_len):	
		matrix[y].extend([0]*(max_len-length[y]))
	return max_len

for cnt in range(101):
	if r+1<=row_len and c+1<= col_len :
		if matrix[r][c] == k:
			result = cnt
			break
	if row_len >= col_len:
		col_len= r_cal(matrix,row_len,col_len)
	else:
		matrix = list(zip(*matrix))
		row_len = r_cal(matrix,col_len,row_len)
		matrix = list(zip(*matrix))
print(result)

	