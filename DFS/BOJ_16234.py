from collections import deque

N, L, R = map(int, input().split())
populationMap = []
for i in range(N):
    populationMap.append(list(map(int, input().split())))

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def bfs():
    unionMap = [[0 for i in range(N)] for j in range(N)]
    visit = [[0 for i in range(N)] for j in range(N)]
    unionNum = 0
    searchNation = deque()
    searchNation.append((0,0))
    while searchNation:
        r, c = searchNation.popleft()
        unionMap[r][c] = unionNum
        visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >=N or visit[nr][nc] == 1:
                continue
            if L <= abs(populationMap[r][c] - populationMap[nr][nc]) <= R:
                flag = False
                unionMap[nr][nc] = unionMap[r][c]
                searchNation.append((nr,nc))
                visit[nr][nc] = 1
            else:
                unionMap[nr][nc] = unionMap[r][c] + 1
                searchNation.append((nr,nc))
    return unionMap

visit = [[0 for i in range(N)] for j in range(N)]
def dfs(r,c,population,cnt):
    print(population)
    print(cnt)
    visit[r][c] = 1
    population += populationMap[r][c]
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= N or visit[nr][nc] == 1:
            continue
        if unionMap[nr][nc] == unionMap[r][c]:
            dfs(nr, nc, population, cnt )
    return population // cnt

def movePeople(num, currentPop):
    for i in range(N):
        for j in range(N):
            if populationMap[i][j] == num:
                populationMap[i][j] = currentPop
                print(populationMap, i,j)
                print(currentPop)

flag = True
changeCnt = 0
# while flag == True:
#     unionMap = bfs()
#     for r in range(N):
#         for c in range(N):
#             if visit[r][c] == 0:
#                 population = 0
#                 cnt = 0
#                 currentPop = dfs(r,c, population,cnt)
#                 movePeople(populationMap[r][c], currentPop)
#     changeCnt += 1
#     flag = True
unionMap = bfs()
print(unionMap)
for r in range(N):
    for c in range(N):
        if visit[r][c] == 0:
            population = 0
            cnt = 0
            currentPop = dfs(r,c, population,cnt)
            print(currentPop)
            movePeople(populationMap[r][c], currentPop)
changeCnt += 1
# print(populationMap)
# print(unionMap)
