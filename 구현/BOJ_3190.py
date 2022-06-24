from collections import deque

N = int(input())
K = int(input())

box = [[0 for _ in range(N+1)] for i in range(N+1)]
snake = deque([[0,0]])
snakeHead = [0,0]
cnt = 0

for i in range(K):
    r, c = map(int, input().split())
    box[r][c] = 1

L = int(input())

def moveRightSnake():
    for i in range(snake):
        snakeHead[1] += 1
        if snakeHead[1] >= N:
            return cnt
        snake.append(snakeHead)
        if box[snakeHead[0]][snakeHead[1]] != 1:
            snake.pop()

def moveLeftSnake():
    for i in range(snake):
        snakeHead[1] -= 1
        if snakeHead[1] <= 0:
            return cnt
        snake.append(snakeHead)
        if box[snakeHead[0]][snakeHead[1]] != 1:
            snake.pop()

def moveUpSnake():
    for i in range(snake):
        snakeHead[0] -= 1
        if snakeHead[0] <= 0:
            return cnt
        snake.append(snakeHead)
        if box[snakeHead[0]][snakeHead[1]] != 1:
            snake.pop()

def moveDownSnake():
    for i in range(snake):
        snakeHead[0] += 1
        if snakeHead[0] >= N:
            return cnt
        snake.append(snakeHead)
        if box[snakeHead[0]][snakeHead[1]] != 1:
            snake.pop()


endTime = 0
for i in range(L):
    x, y = map(int, input().split())
    continueTime = x - endTime
    for j in range(continueTime):
        moveSnake()
