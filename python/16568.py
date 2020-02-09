n,a,b=map(int,input().split())
m=1e12
a+=1;b+=1
print(n//a+1)
for i in range(n//a+1):
    # r은 n에서 a*i를 뺀 값
    r=n-i*a

    # i에 r을 b로 나눈 몫과 나머지를 더한다.
    # 즉 i번째 값에서 (n에서 a를 i만큼 뺀 값에서)
    # b만 사용하였을 때 제일 작은 횟수가 걸린 것을 찾는다.
    m=min(m,i+r//b+r%b)

    print("i = ",i,"r = ",r,"m = ",m)
    print("r//b = ",r//b,"r%b = ",r%b)
    print("-------------------------------------")
    
print(m)