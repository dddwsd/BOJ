def dfs(count, total):
    
    global answer
    print()
    print("count = ",count)
    print("total = ",total)
    if count >= N+1:
        print(111)
        if answer < total:
            answer = total
        return
    if count+4 <= N:
        # 길이를 넘어가지 않는다면
        print(222)
        dfs(count+4, eval(str(total) + arr[count] + str(eval(arr[count+1:count+4]))))

    print(333)
    dfs(count+2, eval(str(total) + arr[count:count+2]))
    
N = int(input())
arr = input()
answer = -2**31
dfs(1,int(arr[0]))
print(answer)