N,M = map(int, input().split())

tree = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)

for i in range(M):
    x, y = map(int, input().split())
    tree[x][y] = tree[y][x] = 1

result = []
cnt = 0
vis = 0

def dfs(x):
    visit[x] = 1
    for i in range(1, N+1):
        if tree[x][i] == 1 and visit[i] == 0:
            dfs(i)

for i in range(1,N+1):
    if visit[i] == 1:
        continue
    dfs(i)
    cnt += 1

print(cnt)

