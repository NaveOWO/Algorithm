from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
virus = []
wall = []
point = deque()
safe_zone = 0

for i in range(n):
    virus.append(list(map(int, input().split())))
    for j in range(m):
        if virus[i][j] == 0:
            wall.append((i,j))
        if virus[i][j] == 2:
            point.append((i,j))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    global safe_zone
    cnt = 0
    while current_point:
        x, y = current_point.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if experience[nx][ny] == 0:
                experience[nx][ny] = 2
                current_point.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if experience[i][j] == 0:
                cnt += 1

    if cnt > safe_zone:
        safe_zone = cnt

for p in list(combinations(wall,3)):
    experience = copy.deepcopy(virus)
    current_point = copy.deepcopy(point)
    for r,c  in list(p):
        experience[r][c] = 1
    bfs()

print(safe_zone)


