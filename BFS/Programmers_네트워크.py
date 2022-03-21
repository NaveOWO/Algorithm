from collections import deque


def solution(n, computers):
    connect = deque()
    visit = [[0 for i in range(n)] for j in range(n)]
    cnt = 0

    def bfs():
        while connect:
            r, c = connect.popleft()
            visit[r][c] = 1
            for i in range(len(computers[c])):
                if i == c:
                    continue
                if computers[c][i] == 1 and visit[c][i] == 0:
                    connect.append((c, i))
                    visit[c][i] = 1

    for i in range(n):
        for j in range(len(computers[i])):
            if i == j:
                visit[i][j] = 1
                continue
            if computers[i][j] == 1 and visit[i][j] == 0:
                connect.append((i, j))
                bfs()
                cnt += 1

    not_visited = 0
    for i in range(n):
        if computers[i].count(1) == 1:
            not_visited += 1

    return cnt + not_visited