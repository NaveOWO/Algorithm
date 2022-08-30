import copy

N, M = map(int, input().split())

global office
office = [[] for _ in range(N)]
for i in range(N):
    office[i] = list(map(int, input().split()))

def searchRight(r,c, tempOffice):
    cnt = 0
    while True:
        c += 1
        if c >= M :
            break
        if tempOffice[r][c] == 0:
            tempOffice[r][c] = '#'
            cnt += 1
        elif tempOffice[r][c] == 6:
            break
    return tempOffice, cnt

def searchLeft(r,c,tempOffice) :
    cnt = 0
    while True:
        c -= 1
        if c < 0:
            break
        if tempOffice[r][c] == 0:
            tempOffice[r][c] = '#'
            cnt += 1
        elif tempOffice[r][c] == 6:
            break
    return tempOffice, cnt

def searchUp(r,c,tempOffice):
    cnt = 0
    while True:
        r -= 1
        if r < 0:
            break
        if tempOffice[r][c] == 0:
            tempOffice[r][c] = '#'
            cnt += 1
        elif tempOffice[r][c] == 6:
            break
    return tempOffice, cnt

def searchDown(r,c,tempOffice):
    cnt = 0
    while True:
        r += 1
        if r >= N:
            break
        if tempOffice[r][c] == 0:
            tempOffice[r][c] = '#'
            cnt += 1
        elif tempOffice[r][c] == 6:
            break
    return tempOffice, cnt

def cctvOne(r,c):
    global office
    results = {}
    tempOffice = copy.deepcopy(office)
    rightOffice,rightCnt = searchRight(r,c,tempOffice)
    results[rightCnt] = rightOffice
    tempOffice = copy.deepcopy(office)
    leftOffice, leftCnt = searchLeft(r,c,tempOffice)
    results[leftCnt] = leftOffice
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r,c,tempOffice)
    results[upCnt] = upOffice
    tempOffice = copy.deepcopy(office)
    downOffice, downCnt = searchDown(r,c,tempOffice)
    results[downCnt] = downOffice
    maxCnt = 0
    for key in results:
        if key > maxCnt:
            maxCnt = key
            office = results[key]

def cctvTwo(r,c):
    global office
    results = {}
    tempOffice = copy.deepcopy(office)
    rightOffice, rightCnt = searchRight(r,c,tempOffice)
    leftOffice, leftCnt = searchLeft(r,c,rightOffice)
    results[rightCnt+leftCnt] = leftOffice
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r,c,tempOffice)
    downOffice, downCnt = searchDown(r,c,upOffice)
    results[upCnt+downCnt] = downOffice
    # print(results)
    maxCnt = 0
    for key in results:
        if key > maxCnt:
            maxCnt = key
            office = results[key]

def cctvThree(r,c):
    global office
    results = {}
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r, c, tempOffice)
    rightOffice, rightCnt = searchRight(r, c, upOffice)
    results[upCnt + rightCnt] = rightOffice
    tempOffice = copy.deepcopy(office)
    rightOffice, rightCnt = searchRight(r, c, tempOffice)
    downOffice, downCnt = searchDown(r, c, rightOffice)
    results[rightCnt + downCnt] = downOffice
    tempOffice = copy.deepcopy(office)
    downOffice, downCnt = searchDown(r, c, tempOffice)
    leftOffice, leftCnt = searchLeft(r, c, downOffice)
    results[downCnt + leftCnt] = leftOffice
    tempOffice = copy.deepcopy(office)
    leftOffice, leftCnt = searchLeft(r, c, tempOffice)
    upOffice, upCnt = searchUp(r, c, leftOffice)
    results[leftCnt + upCnt] = upOffice
    maxCnt = 0
    print(results)
    for key in results:
        if key > maxCnt:
            maxCnt = key
            office = results[key]

def cctvFour(r,c):
    global office
    results = {}
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r, c, tempOffice)
    rightOffice, rightCnt = searchRight(r, c, upOffice)
    leftOffice, leftCnt = searchRight(r, c, rightOffice)
    results[upCnt + rightCnt + leftCnt] = leftOffice
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r, c, tempOffice)
    rightOffice, rightCnt = searchRight(r, c, upOffice)
    downOffice, downCnt = searchDown(r, c, rightOffice)
    results[upCnt + rightCnt + downCnt] = downOffice
    tempOffice = copy.deepcopy(office)
    rightOffice, rightCnt = searchRight(r,c,tempOffice)
    downOffice, downCnt = searchDown(r, c, rightOffice)
    leftOffice, leftCnt = searchLeft(r, c, downOffice)
    results[rightCnt + downCnt + leftCnt] = leftOffice
    tempOffice = copy.deepcopy(office)
    downOffice, downCnt = searchDown(r,c,tempOffice)
    leftOffice, leftCnt = searchLeft(r, c, downOffice)
    upOffice, upCnt = searchUp(r, c, leftOffice)
    results[downCnt + leftCnt + upCnt] = upOffice
    maxCnt = 0
    for key in results:
        if key > maxCnt:
            maxCnt = key
            office = results[key]

def cctvFive(r,c):
    global office
    tempOffice = copy.deepcopy(office)
    downOffice, downCnt = searchDown(r,c,tempOffice)
    leftOffice, leftCnt = searchLeft(r, c, downOffice)
    upOffice, upCnt = searchUp(r, c, leftOffice)
    rightOffice, rightCnt = searchRight(r,c,upOffice)

    office = upOffice



for i in range(N):
    for j in range(M):
        if office[i][j] == 1:
            cctvOne(i,j)
            print(office,"1")
        elif office[i][j] == 2:
            cctvTwo(i,j)
            print(office,"2")
        elif office[i][j] == 3:
            cctvThree(i,j)
            print(office,"3")
        elif office[i][j] == 4:
            cctvFour(i,j)
            print(office,"4")
        elif office[i][j] == 5:
            cctvFive(i,j)
            print(office,"5")

zeroCnt = 0
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            zeroCnt += 1

print(zeroCnt)

# 같을 때 어떻게 해야되냐?



