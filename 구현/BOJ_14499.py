N, M, x, y, K = map(int, input().split())

mapBoard = []
for i in range(N):
    mapBoard.append(list(map(int, input().split())))

orderList = list(map(int, input().split()))

dice = {'upDown' : [0,0], 'frontBack' : [0,0], 'side' : [0,0]}

def moveDice(direction):
    if direction == 1 or direction == 2:
        currentSide = dice['upDown']
        currentUpDown = dice['side']
        dice['upDown'] = currentUpDown
        dice['side'] = currentSide
    else:
        currentUpDown = dice['frontBack']
        currentFrontBack = dice['upDown']
        dice['upDown'] = currentUpDown
        dice['frontBack'] = currentFrontBack
    return

global r, c
r, c = 0, 0
def moveMapBoard(direction):
    global r, c
    if direction == 1:
        c += 1
    elif direction == 2:
        c -= 1
    elif direction == 3:
        r -= 1
    else:
        r += 1

for i in range(K):
    moveDice(orderList[i])
    moveMapBoard(orderList[i])
    print(r,c)
    if r >= N or r < 0 or c >= M or c < 0:
        continue
    if mapBoard[r][c] == 0:
        if orderList[i] == 1 or orderList[i] == 4:
            mapBoard[r][c] = dice['upDown'][0]
            topNum = dice['upDown'][0]
        else:
            mapBoard[r][c] = dice['upDown'][1]
            topNum = dice['upDown'][1]
    else:
        if orderList[i] == 1 or orderList[i] == 4:
            dice['upDown'][0] = mapBoard[r][c]
            topNum = dice['upDown'][0]
        else:
            dice['upDown'][1] = mapBoard[r][c]
            topNum = dice['upDown'][1]
        mapBoard[r][c] = 0
    print(topNum)
    print(dice)


