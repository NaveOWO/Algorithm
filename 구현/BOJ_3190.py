N = int(input())
K = int(input())

box = [[0 for _ in range(N)] for i in range(N)]
for i in range(K):
    c, r = map(int, input().split())
    box[r][c] = 1

L = int(input())
snake = [[0,0]]
direction = right

game = proceed
def moveSnake(time):
    for i in range(time):
        if direction == right:
            for s in range(len(snake)):
                if s == 0 and snake[s][1] == N-1:
                    game = stop
                    return cnt
                if s != 0 and snake[s][1] == N-1:
                    snake[s][]
                snake[s][1] += 1
        if box[head[0],head[1]] == 1:
            box[head[0],head[1]] = 0
            continue
        tail



for i in range(L):
    x, c = map(int, input().split())
    for j in range(x):
        if