x,y = input().split()
x = int(x)
y = int(y)

a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]
num = int(0)
# 1 + 7 = 월
for i in range(1,x):
    if i in a:
        num = num + 31
    if i in b :
        num = num + 30
    if i in c:
        num = num + 28
num = num + y

num2 = num%7
if num2 == 1:
    print("MON")
elif num2 == 2:
    print("TUE")
elif num2 == 3:
    print("WED")
elif num2 == 4:
    print("THU")
elif num2 == 5:
    print("FRI")
elif num2 == 6:
    print("SAT")
elif num2 == 0:
    print("SUN")

        
