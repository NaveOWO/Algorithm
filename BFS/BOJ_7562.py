from collections import deque
T = int(input())

dr = [1,2,2,1,-1,-2,-2,-1]
dc = [2,1,-1,-2,-2,-1,1,2]

def bfs():

    while move:
        r, c = move.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if chess[nr][nc] == 0:
                move.append((nr,nc))
                chess[nr][nc] = chess[r][c] + 1
            if nr == a and nc == b:
                return chess[nr][nc]



answer = []
for i in range(T):
    n = int(input())
    chess = [[0 for i in range(n)] for i in range(n)]
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    chess[x][y] = 1
    move = deque()
    move.append((x,y))
    bfs()
    answer.append(bfs()-1)
for i in answer:
    print(i)


