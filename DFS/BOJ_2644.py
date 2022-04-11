n = int(input())
a, b = map(int, input().split())

family = [[0]*(n+1) for _ in range((n+1))]
visit = [0]*(n+1)

for i in range(int(input())):
    x, y = map(int, input().split())
    family[x][y] = family[y][x] = 1

cnt = 0
ans = 0

def dfs(p, cnt):
    global ans
    visit[p] = 1
    for i in range(1,n+1):
        if family[p][i] == 1 and visit[i] == 0:
            visit[i] = 1
            if i == b:
                ans = cnt + 1
                return ans
            dfs(i, cnt+1)
dfs(a,cnt)

print(ans if ans > 0 else -1)


origin = [8,9]