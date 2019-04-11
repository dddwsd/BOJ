a = input()
for i in range(1,len(a)+1):
    print(a[i-1],end="")
    if i%10 == 0:
        print()
    
