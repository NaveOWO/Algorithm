from collections import deque

m, n, k = map(int, input().split())
paper = [[0 for i in range(m)] for j in range(n)]
whiteZone = deque()
cnt = 0
allArea = []
area = 0


def paintSquare(x,y,z,r):
    for i in range(z-x):
        for j in range(r-y):
            paper[x+i][y+j] = 1

for i in range(k):
    x,y,z,r = map(int, input().split())
    paintSquare(x,y,z,r)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():
    area = 0
    while whiteZone:
        x, y = whiteZone.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if paper[nx][ny] == 0:
                whiteZone.append((nx,ny))
                paper[nx][ny] = 1
                area += 1
    allArea.append(area+1)

for x in range(n):
    for y in range(m):
        if paper[x][y] == 0:
            cnt += 1
            whiteZone.append((x,y))
            paper[x][y] = 1
            bfs()

allArea.sort()
print(cnt)
for i in allArea:
    print(i,end = ' ')