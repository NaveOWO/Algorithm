from collections import deque

n,m = map(int, input().split())
shark = []
for i in range(n):
    shark.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if shark[i][j] == 1:
            q.append((i,j))

nx = [0,1,1,1,0,-1,-1,-1]
ny = [1,1,0,-1,-1,-1,0,1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            if shark[dx][dy] == 0:
                q.append((dx,dy))
                shark[dx][dy] = shark[x][y] + 1
bfs()
long = 0
for i in range(n):
    for j in range(m):
        long = max(shark[i][j], long)
print(long-1)
