# 수빈 동생 -> 숨바꼭질
# 수빈 : 0 ~ 100,000 사이에 N -> 걷거나 순간이동 
# 걷기 : -1 or +1 / 순간이동 2*현재위치
# 동생 : 0 ~ 100,000 사이에 K

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
n,k = map(int,input().split())
stack = set()
stack.add(n)
cnt = 0
visited = [0 for _ in range(100001)]
# bfs - 최소 길이
# 100000까지 이므로 +1해서 배열할당
# set + visited + case미리 계산 을 사용하여 제일 빠른 속도
visited[n] = 1
def find():
    global cnt
    global visited
    global stack
    while True:
        stack2 = set()
        cnt += 1
        for i in stack:
            case1 = i-1
            case2 = i+1
            case3 = 2*i
            if case1 >= 0 and visited[case1] == 0:
                if case1 == k:
                    print(cnt)
                    return
                visited[case1] = 1
                stack2.add(case1)
            if case2< 100001 and visited[case2] == 0:
                if case2 == k:
                    print(cnt)
                    return
                visited[case2] = 1
                stack2.add(case2)
            if case3 < 100001 and visited[case3] == 0:
                if case3 == k:
                    print(cnt)
                    return
                visited[case3] = 1
                stack2.add(case3)
        stack = stack2
            
    


if k > n :
    find()
elif k == n:
    print(0)
else:
    while True:
        if n == k:
            print(cnt)
            break
        n -= 1
        cnt += 1




    
