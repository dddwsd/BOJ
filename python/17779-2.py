'''
지역 : n x n
(r,c) : r행 c열  

구역 : 5개로 나눔

선거구를 나누는 방법
1. 기준점 (x,y)와 경계의 길이 d1,d2를 정한다
2. 경계선
	(1). (x,y) , (x+1,y-1), . . . (x+d1,y-d1)
	(2). (x,y) , (x+1,y+1), . . . (x+d2,y+d2)
	(3). (x+d1,y-d1), (x+d1+1,y-d1+1), . . . ,(x+d1+d2,y-d1+d2)
	(4). (x+d2,y+d2), (x+d2+1,y+d2-1), . . . ,(x+d2+d1,y+d2-d1)
3. 경계선과 경계선 안에 포함되어 있는 5번 선거구이다.
4. 5번 선거구에 포함되지 않은 구역(r,c)의 선거구 번호는 다음 기준을 따른다
	(1). 1 <= r < x+d1, 1 <= c <= y
	(2). 1 <= r <= x+d2, y < c <= n
	(3). x+d1 <= r <= n, 1 <= c < y-d1+d2
	(4). x+d2 < r <= n, y-d1+d2 <= c <= n
'''
'''
알고리즘
1. x,y d1,d2를 정한다
- 1 <= d1, d2
- 1 < = d1+d2 < n+1
- 1 <= x < x+d1+d2
- 1 <= y-d1 < y < y+d2 <= n
2. x,y d1,d2가 주어진 조건에 성립하는지 확인한다.
3. 성립한다면 선거구를 나누어서 각 선거구의 수를 구한다.
4. 선거구의 max값과 min값의 차이를 result와 비교하여 작을 경우 갱신한다.

(1). 1 <= r < x+d1, 1 <= c <= y
(2). 1 <= r <= x+d2, y < c <= n
(3). x+d1 <= r <= n, 1 <= c < y-d1+d2
(4). x+d2 < r <= n, y-d1+d2 <= c <= n
'''
n = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
for y in range(1,n+1):
	matrix[y][1:] = list(map(int,input().split()))

def find_area5(x,y,d1,d2):
	dic = {}
	dic[x] = [y]
	for i in range(1,d1+d2):
		if i <= d1:
			start = y-i
		else:
			start += 1
		if i <= d2:
			end = y+i
		else:
			end -= 1
		dic[x+i] = [j for j in range(start,end+1)]
	dic[x+d1+d2] = [y-d1+d2]
	return dic

def solution(x,y,d1,d2):
	area5 = find_area5(x,y,d1,d2)
	temp = [0]*5
	for r in range(1,n+1):
		for c in range(1,n+1):
			if r in area5 and c in area5[r]:
				temp[4] += matrix[r][c]
			elif 1 <= r < x+d1 and 1 <= c <= y:
				temp[0] += matrix[r][c]
			elif 1 <= r <= x+d2 and y < c <= n:
				temp[1] += matrix[r][c]
			elif x+d1 <= r <= n and 1 <= c < y-d1+d2:
				temp[2] += matrix[r][c]
			elif x+d2 < r <= n and y-d1+d2 <= c <= n:
				temp[3] += matrix[r][c]
	return max(temp) - min(temp)

result = 10 ** 9
for d1 in range(1,n-1):
	for d2 in range(1,n-1):
		if 2<= d1+d2 <= n-1:
			for x in range(1,n-1):
				if 1 <= x < x+d1+d2 <= n:
					for y in range(2,n):
						if 1 <= y-d1 < y <y+d2 <= n:
							result = min(result,solution(x,y,d1,d2))
print(result)
