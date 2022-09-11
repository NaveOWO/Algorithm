N, M = map(int, input().split())
office = [[] for i in range(N)]
for i in range(N):
    office.append(list(map(int, input().split())))

def dfs(r,c,direction):
    