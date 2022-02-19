import sys
std = sys.stdin.readline
sys.setrecursionlimit(10000)


T = int(std())
field = []

def dfs(row, column):
    x = [0,1,0,-1]
    y = [1,0,-1,0]

    field[row][column] = 0
    for i in range(4):
        nr = row + y[i]
        nc = column + x[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M :
            continue
        if field[nr][nc] == 1:
            dfs(nr, nc)

for i in range(T):
    M,N,K = map(int, std().split())
    field = []
    cnt = 0
    for i in range(N):
        field.append([0 for i in range(M)])
    for i in range(K):
        column, row = map(int, std().split())
        field[row][column] = 1
    for row in range(N):
        for column in range(M):
            if field[row][column] == 1:
                dfs(row,column)
                cnt += 1
    print(cnt)

