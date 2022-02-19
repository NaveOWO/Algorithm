n = int(input())
m = int(input())

tree = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    tree[a][b] = tree[b][a] = 1

result = []

def dfs(x):
    visit[x] = 1
    for i in range(1,n+1):
        if tree[x][i] == 1 and visit[i] == 0:
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))