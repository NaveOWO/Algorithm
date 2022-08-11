from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
city = []
chicken = []
for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(len(city[i])):
        if city[i][j] == 2:
            chicken.append((i,j))
chickenCombi = list(combinations(chicken, M))
for i in range(len(chickenCombi)):
    chickenCombi[i] = deque(chickenCombi[i])

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            city[i][j] = 0

def removeChicken(combi, tempCity):
    for r in range(N):
        for c in range(N):
            if tempCity[r][c] == 2 and (r,c) not in combi:
                tempCity[r][c] == 0
    return tempCity

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def getCityDistance(C,tempCity):
    cityDistance = 0
    print(C)
    while C:
        r,c = C.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N :
                continue
            if tempCity[nr][nc] == 0:
                C.append((nr,nc))
                tempCity[nr][nc] += tempCity[r][c]
            elif tempCity[nr][nc] == 1:
                tempCity[nr][nc] += tempCity[r][c]
                cityDistance += tempCity[nr][nc]
    return cityDistance

resultList = []
cnt = 0
for i in range(len(chickenCombi)):
    tmpCity = copy.deepcopy(city)
    tmpCity = removeChicken(chickenCombi[i], tmpCity)
    resultList.append(getCityDistance(chickenCombi[i],tmpCity))
    cnt += 1
