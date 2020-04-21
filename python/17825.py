num = list(map(int,input().split()))
# road set
road = {}
road['red'] = [i for i in range(0,42,2)]
road['b10'] = [10,13,16,19,25,30,35,40]
road['b20'] = [20,22,24,25,30,35,40]
road['b30'] = [30,28,27,26,25,30,35,40]

# length set
length = {}
for key,val in road.items():
  length[key] = len(val)
# user = [type, current position]
user = {}
for i in range(4):
  user[i] = ['red',0]
# user, cur_posi, val, last
stack = [[user,[0,0,0,0],0,1]]

# move position
def move(name,cur):
  # '도착'에 도착하면 out
  if cur >= length[name]:
    return ['out',0],0
  # red에서 10 , 20 , 30 에 도착하는 경우 road_type을 변경하고 cur도 변경
  elif name == 'red':
    if road[name][cur] == 10:
      return ['b10',0],10
    elif road[name][cur] == 20:
      return ['b20',0],20
    elif road[name][cur] == 30:
      return ['b30',0],30
  # 그냥 갈길 가는 경우 
  return [name,cur],road[name][cur]


'''
값이 같으면 -> 같은 자리
예외사항
1. 값이 같지만 길이 다르면 다른 것
  - 16 (b10, red)
  - 22 (b20,red)
  - 24 (b20,red)
  - 26 (b30,red)
  - 28 (b30,red)
2. 값이 같으면 같을 수도 다를 수도
  - 30
    - [b30,0]
    - [b10,5] and [b20,4] and b[30,5]
'''
case = [['b10',5],['b20',4],['b30',5]]
def check(plus, cur_val, after_user, user):
  
  if plus == 0:
    return 1
  else:
    if plus in cur_val:
      if plus in [16,22,24,26,28]: 
        if after_user not in user:
          return 1
        else:
          return 0
      elif plus == 30:
        if after_user == ['b30',0] and after_user not in user:
          return 1
        if after_user in case and case[0] not in user and case[1] not in user and case[2] not in user:
          return 1
      else:
        return 0
    else:
      return 1

result = 0


# num에 저장된 step 순서대로 진행
cnt = 0
for index, step in enumerate(num):
  temp = []
  # stack에 있는 것들을 갖고 진행 -> brute force
  for user,cur_val,val,last in stack:
    
    cnt += 1
    # last에는 필드에 나간 말의 개수
    for i in range(last):
      # out된 말은 그냥 무시
      if user[i][0] == 'out':
        continue
      # move 함수를 통해 현재 말의 다음 위치를 구함
      after_user,plus = move(user[i][0],user[i][1]+step)
      # 말이 이동후에 out이거나 이동하려고 하는 자리에 다른 말이 없는 경우는 추가
      # 말이 이동하려고 하는 자리에 out이 아닌 다른 말이 있는 경우 x
      if check(plus, cur_val, after_user, list(user.values())) == 1:
        t_user = user.copy()
        t_user[i] = after_user
        t_cur_val = cur_val.copy()
        t_cur_val[i] = plus
        result = max(result,val+plus)
        temp.append([t_user,t_cur_val,val+plus,last])    
    # 4개의 말이 모두 나가있지 않은 경우
    if last < 4 and index != 0 :
      # 출발에 있는 말을 내보낸다.
      after_user,plus = move('red',step)
      # 이동한 후의 위치에 다른 말이 없을 경우 추가
      if check(plus, cur_val, after_user, user.values()) == 1:
        t_user = user.copy()
        t_user[last] = after_user
        t_cur_val = cur_val.copy()
        t_cur_val[last] = plus
        result = max(result,val+plus)
        temp.append([t_user,t_cur_val,val+plus,last+1])
  # stack update
  stack = temp.copy()
# 구해진 경우의 수 중에 제일 큰 값을 찾는다.
print(result)