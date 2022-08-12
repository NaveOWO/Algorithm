from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
city = []
chickenList = []
CHICKEN = 2
HOME = 1

for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(len(city[i])):
        if city[i][j] == CHICKEN:
            chickenList.append((i,j))

chickenCombiList = list(combinations(chickenList, M))

for i in range(len(chickenCombiList)):
    chickenCombiList[i] = deque(chickenCombiList[i])

def removeChicken(tempCity, chickenCombi):
    for r in range(N):
        for c in range(N):
            if tempCity[r][c] == CHICKEN and (r,c) not in chickenCombi:
                tempCity[r][c] = 0
    return tempCity

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def getCityDistance(chickenCombi, tempCity):
    cityDistance = 0
    visit = [[0 for _ in range(N)] for i in range(N)]
    while chickenCombi:
        r,c = chickenCombi.popleft()
        visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visit[nr][nc] == 1:
                continue
            if tempCity[nr][nc] == 0:
                chickenCombi.append((nr,nc))
                tempCity[nr][nc] = tempCity[r][c] + 1
                continue
            if tempCity[nr][nc] == HOME:
                chickenCombi.append((nr,nc))
                tempCity[nr][nc] = tempCity[r][c] + 1
                cityDistance += tempCity[nr][nc]-2
    return cityDistance




resultList = []
for i in range(len(chickenCombiList)):
    tempCity = copy.deepcopy(city)
    tempCity = removeChicken(tempCity, chickenCombiList[i])
    resultList.append(getCityDistance(chickenCombiList[i], tempCity))

print(min(resultList))



