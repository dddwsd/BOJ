'''
키로거 - 사용자가 키보드를 누른 명령을 모두 기록
강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호 알아낼 수 있다.
비밀번호 창에서 입력한 키가 주어졌을 때
-> 비밀번호를 알아내는 프로그램

백스페이스 : - / 커서의 바로 앞에 글자가 존재한다면 그 글자를 지운다
화살표의 입력은 <와 >로 주어진다.

커서의 위치를 움직일 수 있다면, 왼쪽 or 오른쪽으로 1만큼 움직인다.

나머지 문자는 비밀번호의 일부
나중에 백 스페이스를 통해 지울수는 있다.
커서의 위치가 줄의 마지막이 아니라면, 그 문자를 입력하고 커서는 오른쪽으로 한 칸 이동한다.
'''

tc = int(input())
for _ in range(tc):
    string = list(input())
    result = [0 for _ in range(len(string)+1)]
    cur = 0
    length = 0
    for item in string:
        
        if item == '<' :
            if cur > 0:
                cur -= 1
        elif item == '>':
            if cur < length:
                cur += 1
        elif item == '-':
            if cur >0:
                result.pop(cur-1)
                length -= 1
                cur -= 1
        else:
            result[cur+1:] = result[cur:-1]
            result[cur] = item
            length += 1
            cur += 1
    print("".join(result[:length]))
    

            