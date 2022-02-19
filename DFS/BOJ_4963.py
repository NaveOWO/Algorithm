from sys import stdin
std = stdin.readline

def dfs(row, column):
    x = [0,1,1,1,0,-1,-1,-1]
    y = [1,1,0,-1,-1,-1,0,1]

    island[row][column] = 0
    for i in range(8):
        nrow = row + x[i]
        ncolumn = column + y[i]
        if nrow < 0 or nrow >= h or ncolumn < 0 or ncolumn >= w :
            continue
        if island[nrow][ncolumn] == 1:
            dfs(nrow,ncolumn)

while True:
    island = []
    cnt = 0
    w, h = map(int, std().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        island.append(list(map(int, std().split())))
    for row in range(h):
        for column in range(w):
            if island[row][column] == 1:
                dfs(row,column)
                cnt += 1
    print(cnt)