import copy

N, M = map(int, input().split())

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
    results = []
    tempOffice = copy.deepcopy(office)
    rightOffice,rightCnt = searchRight(r,c,tempOffice)
    tempOffice = copy.deepcopy(office)
    leftOffice, leftCnt = searchLeft(r,c,tempOffice)
    tempOffice = copy.deepcopy(office)
    upOffice, upCnt = searchUp(r,c,tempOffice)

