from collections import deque
m,n = map(int, input().split())

tomato = []
ripe = deque()

for i in range(n):
    tomato.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            ripe.append((i,j))
        if tomato[i][j] == 0:
            cnt += 1

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs():
    min_day = 0
    while ripe:
        r,c = ripe.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[r][c] + 1
                min_day = tomato[nr][nc]
                ripe.append((nr,nc))
    return (min_day - 1)
answer = bfs()

not_ripe = 0
if cnt == 0:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                not_ripe += 1
    if not_ripe != 0:
        print(-1)
    else:
        print(answer)