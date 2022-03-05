from sys import stdin
import sys

std = stdin.readline
sys.setrecursionlimit(10000)

N = int(std())
region = []
result = 1
visit = [[0 for _ in range(N)] for i in range(N)]

for i in range(N):
    region.append(list(map(int, std().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(k, x, y):
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if region[nx][ny] > k and visit[nx][ny] == 0:
            dfs(k, nx, ny)

a = max(map(max, region))
k = min(map(min, region))

while k <= a:
    cnt = 0
    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0 and region[x][y] > k:
                dfs(k, x, y)
                cnt += 1
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0
    if cnt > result:
        result = cnt
    k += 1

print(result)

