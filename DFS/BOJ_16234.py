from collections import deque

N,L,R = map(int,input().split())
populationMap = []
for i in range(N):
    populationMap.append(list(map(int, input().split())))
# populationMap의 인구수의 차이가 조건과 맞는지 판단한다--> BFS
# 같은 연합인 나라들을 같은 숫자로 묶는다
# 같은 숫자인 나라들 인구수를 다 더해서 나라의 갯수로 나눈 몫을 구한다
# 위의몫을 나라들한테 나누어준다
# 위의 과정을 할때마다 cnt를 올린다
# 1번조건이 한번이라도 맞으면 flag에 변화주기

unionMap = [[0 for _ in range(N)] for _ in range(N)]
global flag
flag = True
dr = [-1,0,1,0]
dc = [0,1,0,-1]
def getUnionMap(r,c,visit,changeList):
    global flag
    global unionMap
    visit = [[0 for _ in range(N)] for _ in range(N)]
    nations = deque()
    nations.append((r,c))
    while nations:
        r, c = nations.popleft()
        visit[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N or visit[nr][nc] == 1:
                continue
            if L <= abs(populationMap[r][c] - populationMap[nr][nc]) <= R:
                unionMap[nr][nc] = unionMap[r][c]
                nations.append((nr,nc))
                visit[nr][nc] = 1
                changeList.append((nr,nc))
    return [unionMap, changeList]

def getSumPopulation(r,c,visit):
    searchNation = deque()
    searchNation.append((r,c))
    population = populationMap[r][c]
    nations = []
    cnt = 1
    while searchNation:
        r,c = searchNation.popleft()
        visit[r][c] = 1
        nations.append((r,c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N or visit[nr][nc] == 1:
                continue
            if unionMap[nr][nc] == unionMap[r][c]:
                population += populationMap[nr][nc]
                cnt += 1
                searchNation.append((nr,nc))
                visit[nr][nc] = 1
                nations.append((nr,nc))
    return [population // cnt, visit, set(nations)]

def refillPopulationMap(nations,currentPop):
    for item in nations:
        populationMap[item[0]][item[1]] = currentPop

totalChange = 0
while True:
    beforeVisit = [[-1 for _ in range(N)] for _ in range(N)]
    changeList = []
    for i in range(N):
        for j in range(N):
            if beforeVisit[i][j] == 0:
                unionMap, changeList = getUnionMap(i,j,beforeVisit, changeList )
                print(changeList)
    if len(changeList) == 0:
        break
    afterVisit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if afterVisit[i][j] == 0:
                currentPop, afterVisit, nations = getSumPopulation(i,j,afterVisit)
                refillPopulationMap(nations,currentPop)
    if flag == False:
        break

    totalChange += 1
    print("union")
    for i in range(len(unionMap)):
        print(unionMap[i])
    print("pop")
    for i in range(len(populationMap)):
        print(populationMap[i])
print(totalChange)
