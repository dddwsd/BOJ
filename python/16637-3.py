'''
길이 N 수식
1. 숫자 : 0 ~ 9
2. +, -, x (우선순위 동일 왼쪽에서부터 순서대로)

- 수식에 괄호를 추가하면 괄호안을 먼저 계산
- 괄호안에는 연산자 하나
- 중첩된 괄호는 사용 불가
'''
'''
알고리즘
1. string을 읽으면서 num과 operator로 나누어서 순서대로 넣는다.
2. 순서대로 꺼내면서 계산을 진행하는데 진행은 3개의 경우로 나눈다
	(1). 괄호가 없는 경우
	(2). 괄호가 있는 경우
		- 앞에 2개가 괄호인 경우는 어차피 앞으로 되므로 생각 x
		- 뒤의 2개가 괄호인 경우는 operator랑 num을 1개씩 꺼내고 계산
		- 그 후에 b랑 더함

'''
n = int(input())
string = input()
num,oper = [],[]
# index가 2의 배수이면 num
# index가 2의 배수가 아니면 oper
for i in range(n):
	if i%2 == 0:
		num.append(string[i])
	else:
		oper.append(string[i])

def solution(num,oper,before,a_in,o_in,result):
	# 뒤에 괄호 x
	oper1 = oper[o_in]
	after1 = num[a_in]
	a_in += 1
	o_in += 1
	if a_in == (n//2)+1 and o_in ==(n//2):
		print(before, oper1, after1)
		result[0] = max(result[0], eval(before + oper1 + after1))
		return
	
	solution(num,oper,str(eval(before+oper1+after1)),a_in,o_in,result)
	# 뒤에 괄호 o
	oper2 = oper[o_in]
	after2 = num[a_in]
	after = str(eval(after1+oper2+after2))
	a_in += 1
	o_in += 1
	if a_in == (n//2)+1 and o_in == (n//2):
		result[0] = max(result[0], eval(before + oper1 + after))
		return
	solution(num,oper,str(eval(before+oper1+after)),a_in,o_in,result)

result = [-2**31]
if n == 1:
	print(string)
else:
	solution(num,oper,num[0],1,0,result)
	print(result[0])	