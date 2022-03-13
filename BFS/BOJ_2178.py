from collections import deque
N,M = map(int, input().split())

miro = []
for i in range(N):
    miro.append(list(input()))
    for j in range(M):
        miro[i][j] = int(miro[i][j])

dr = [0,1,0,-1]
dc = [1,0,-1,0]

road = deque()
road.append((0, 0))

def bfs():
    while road:
        r, c = road.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if miro[nr][nc] == 1:
                road.append((nr, nc))
                miro[nr][nc] = miro[r][c] + 1
            if nr == N-1 and nc == M-1:
                return miro[nr][nc]


print(bfs())