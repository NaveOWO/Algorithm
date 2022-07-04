N = int(input())

studentDict = {}
seatList = [[0 for j in range(N+1)] for i in range(N+1)]
for i in range(N*N):
    x = list(map(int, input().split()))
    studentDict[x[0]] = x[1:]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def searchCloseSeat(x,y, searchResult, student):
    cnt = 0
    empty = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        if seatList[nx][ny] in studentDict[student]:
            cnt += 1
            continue
        if seatList[nx][ny] == 0:
            empty += 1
    if len(searchResult) == 0:
        searchResult.append([x,y,cnt,empty])
    else:
        if searchResult[-1][2] < cnt:
            searchResult = [[x,y, cnt,empty]]
        elif searchResult[-1][2] == cnt :
            searchResult.append([x,y,cnt,empty])
    return searchResult

def seatStudent(student, searchResult):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if seatList[i][j] != 0:
                continue
            searchResult = searchCloseSeat(i,j,searchResult,student)
    if len(searchResult) == 1:
        seatList[searchResult[0][0]][searchResult[0][1]] = student
    else:
        searchResult.sort(key = lambda x: (-x[3], x[0], x[1]))
        seatList[searchResult[0][0]][searchResult[0][1]] = student

for key in studentDict:
    searchResult = []
    seatStudent(key, searchResult)

def satisfyScore(x,y):
    likeCnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue
        if seatList[nx][ny] in studentDict[seatList[x][y]]:
            likeCnt += 1
    return likeCnt

result = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        likeStudentCnt = satisfyScore(i,j)
        if likeStudentCnt != 0:
            result += 10**(likeStudentCnt-1)

print(result)
