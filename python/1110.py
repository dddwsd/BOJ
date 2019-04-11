a = int(input())
temp = a
num = 0
while True:
    ten = int(a/10)
    one = a%10
    a = one*10 + (ten+one)%10
    num += 1
    if a == temp:
        print(num)
        break