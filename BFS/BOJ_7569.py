from collections import deque
M,N,H = map(int, input().split())

box = [[] for i in range(H)]
tomato = deque()
raw = 0

# 위,오,아,왼,높이위,높이아래

dr = [1,0,-1,0,0,0]
dc = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]

def bfs():
    while tomato:
        h,r,c = tomato.popleft()
        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if nh < 0 or nr < 0 or nc < 0 or nh >= H or nr >= N or nc >= M:
                continue
            if box[nh][nr][nc] == 0:
                tomato.append((nh,nr,nc))
                box[nh][nr][nc] = box[h][r][c] + 1

for h in range(H):
    for r in range(N):
        box[h].append(list(map(int, input().split())))
        for c in range(M):
            if box[h][r][c] == 1:
                tomato.append((h,r,c))
            if box[h][r][c] == 0:
                raw += 1

max_num = 0
if raw == 0:
    max_num = 0
else:
    bfs()

    flag = True
    for i in range(H):
        if flag == False:
            break
        for j in range(N):
            if flag == False:
                break
            for t in range(M):
                if box[i][j][t] > max_num:
                    max_num = box[i][j][t]
                if box[i][j][t] == -1:
                    max_num = -1
                    flag = False
                    break

if max_num == 0 or max_num == -1:
    print(max_num)
else:
    print(max_num - 1)
