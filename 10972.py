a = int(input())
x = input().split()

y = list(x)


y.sort(reverse = True)
print(x)

if x == y:
    print(-1)
else:
    y.sort()
    print(y)
        

'''
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2


2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1



1 2 3 4 5
1 2 3 5 4
1 2 4 3 5
1 2 4 5 3
1 2 5 3 4
1 2 5 4 3
1 3 2 4 5

1 3 6 5 4 2
1  
'''
