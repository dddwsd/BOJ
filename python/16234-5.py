n, l, r = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]
move_list = [[-1, 0],[1, 0],[0, -1],[0, 1]]#상 하 좌 우
index_map = [[0 for _ in range(n)] for _ in range(n)]
dic, answer = {}, 0

temp_num = 0
for y in range(n):
    for x in range(n):
        index_map[y][x] = temp_num
        dic[temp_num] = [y,x]
        temp_num += 1
temp_list = [i for i in range(temp_num)]

while True:
    union_list = list()
    country = temp_list
    print(temp_list)
    
    while country:
        temp_country = country.pop()
        check = set(list())
        dfs = [temp_country]

        while dfs:
            dfs_country = dfs.pop()
            check.add(dfs_country)
            y, x = dic[dfs_country][0], dic[dfs_country][1]
            for move in move_list:
                next_y, next_x = y + move[0], x + move[1]
                if 0 <= next_y < n and 0 <= next_x < n:
                    if l <= abs(game_map[y][x] - game_map[next_y][next_x]) <= r:
                        if index_map[next_y][next_x] not in check:
                            dfs.append(index_map[next_y][next_x])

        if len(check) > 1:
            union_list.append(check)

        for index in check:
            if index in country:
                country.pop(country.index(index)) 
    if len(union_list) == 0:
        break

    temp = list()
    for union in union_list:
        temp += union
        sum = 0
        for c in union:
            sum += game_map[dic[c][0]][dic[c][1]]
        result = sum // len(union)
        for c in union:
            game_map[dic[c][0]][dic[c][1]] = result
    temp_list = temp
    answer += 1
print(answer)