'''
n개의 섬으로 이루어진 나라

몇개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업 - 두개의 섬에 공장을 세워 물품을 생산하는 일

물품을 생산하다 보면 공장에서 다른 공장으로 생산중이던 물품을 수송해야 할 일이 생긴다.

각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다.

중량제한 초과하면 다리 무너짐

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램
'''

# Union find
from collections import defaultdict
from collections import deque
n,m = map(int,input().split())

bridge = defaultdict(int)
lands = defaultdict(int)

for _ in range(m):
    a,b,c = map(int,input().split())
    bridge[(a,b)] = c
    lands[a] = a
    lands[b] = b
land1,land2 = map(int,input().split())

bridge = sorted(bridge.items(),key=lambda x: (-x[1],x[0]))
result = -1

def find(key):
    if lands[key] == key:
        return key
    lands[key] = find(lands[key])
    return lands[key]

def union(key):
    key1, key2 = key
    key1 = find(key1)
    key2 = find(key2)
    if key1 < key2:
        lands[key2] = key1
    else:
        lands[key1] = key2

for key, val in bridge:
    union(key)
    if find(land1) == find(land2):
        result = val
        break
print(result)