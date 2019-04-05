
a = set([(1,1,3)])
b = set([1,1,3])
list1 = [1,2,3,4,5,5]
list2 = [1,2,3,4,5,5,5]
c = set()
c.add((tuple(list2),tuple(list1)))
# set안에 튜플 넣으면 중복 가능
# set안에 그냥 넣으면 중복 불가능

print(a)
print(b)
print(c)
