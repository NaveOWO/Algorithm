def solution(m, n, board):

    for i in range(m):
        board[i] = list(board[i])
    visit = [[0 for i in range(n)] for i in range(m)]

    def moveBlock() :
        while True:
            move = 0
            for i in range(m-1):
                for j in range(n):
                    if visit[i][j] == 0 and visit[i+1][j] == 1:
                        board[i+1][j] = board[i][j]
                        visit[i+1][j] = 0
                        visit[i][j] = 1
                        board[i][j] = ''
                        move += 1
            if move == 0:
                for i in range(m):
                    for j in range(n):
                        if visit[i][j] == 1 and board[i][j] != '':
                            board[i][j] = ''
                return board
        return board

    cnt = 0

    while True:
        rotate = 0
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] == '':
                    continue
                if board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                    cnt += [visit[r][c], visit[r][c+1], visit[r+1][c], visit[r+1][c+1]].count(0)
                    visit[r][c], visit[r][c+1], visit[r+1][c], visit[r+1][c+1] = 1, 1, 1, 1
                    rotate += 1
                    # print(r, c)
        # print(board)
        if rotate == 0:
            break
        moveBlock()


    return cnt