from collections import deque

N = int(input())
K = int(input())

box = [[0 for _ in range(N+1)] for i in range(N+1)]
snake = deque([[1,1]])
snakeHead = [1,1]
global isStop,cnt
cnt = 0
isStop = False

for i in range(K):
    r, c = map(int, input().split())
    box[r][c] = 1

D = int(input())


def moveRightSnake():
    global isStop, cnt
    snakeHead[1] += 1
    if [snakeHead[0],snakeHead[1]] in snake or snakeHead[1] >= N+1:
        isStop = True
        return cnt
    snake.append([snakeHead[0],snakeHead[1]])
    cnt += 1
    if box[snakeHead[0]][snakeHead[1]] != 1:
        snake.popleft()
    else:
        box[snakeHead[0]][snakeHead[1]] = 0

def moveLeftSnake():
    global isStop, cnt
    snakeHead[1] -= 1
    if [snakeHead[0],snakeHead[1]] in snake or snakeHead[1] <= 0:
        isStop = True
        return cnt
    snake.append([snakeHead[0],snakeHead[1]])
    cnt += 1
    if box[snakeHead[0]][snakeHead[1]] != 1:
        snake.popleft()
    else:
        box[snakeHead[0]][snakeHead[1]] = 0

def moveUpSnake():
    global isStop, cnt
    snakeHead[0] -= 1
    if [snakeHead[0],snakeHead[1]] in snake or snakeHead[0] <= 0:
        isStop = True
        return cnt
    snake.append([snakeHead[0],snakeHead[1]])
    cnt += 1
    if box[snakeHead[0]][snakeHead[1]] != 1:
        snake.popleft()
    else:
        box[snakeHead[0]][snakeHead[1]] = 0

def moveDownSnake():
    global isStop, cnt
    snakeHead[0] += 1
    if [snakeHead[0],snakeHead[1]] in snake or snakeHead[0] >= N+1:
        isStop = True
        return cnt
    snake.append([snakeHead[0],snakeHead[1]])
    cnt += 1
    if box[snakeHead[0]][snakeHead[1]] != 1:
        snake.popleft()
    else:
        box[snakeHead[0]][snakeHead[1]] = 0


endTime = 0
direction = 'right'
for i in range(D):
    if isStop == True:
        break
    x, y = input().split()
    continueTime = int(x) - endTime
    endTime = int(x)
    for j in range(continueTime):
        if direction == 'right':
            moveRightSnake()
            if isStop == True:
                break
            continue
        if direction == 'left':
            moveLeftSnake()
            if isStop == True:
                break
            continue
        if direction == 'up':
            moveUpSnake()
            if isStop == True:
                break
            continue
        moveDownSnake()
        if isStop == True:
            break
    if y == 'D':
        if direction == 'right':
            direction = 'down'
            continue
        if direction == 'left':
            direction = 'up'
            continue
        if direction == 'up':
            direction = 'right'
            continue
        direction = 'left'
    else:
        if direction == 'right':
            direction = 'up'
            continue
        if direction == 'left':
            direction = 'down'
            continue
        if direction == 'up':
            direction = 'left'
            continue
        direction = 'right'

if isStop == False:
    while isStop == False:
        if direction == 'up':
            moveUpSnake()
        elif direction == 'right':
            moveRightSnake()
        elif direction == 'down':
            moveDownSnake()
        else:
            moveLeftSnake()

print(cnt + 1)
