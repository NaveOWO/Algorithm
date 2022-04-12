from collections import deque


def solution(places):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    result = []
    for t in range(5):
        client = deque()
        visit = [[0 for a in range(5)] for b in range(5)]
        for i in range(5):
            for j in range(5):
                if places[t][i][j] == 'P':
                    client.append((i, j))

        def bfs():
            while client:
                r, c = client.popleft()
                for n in range(4):
                    nr = r + dr[n]
                    nc = c + dc[n]
                    visit[r][c] = 1
                    if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                        continue
                    if places[t][nr][nc] == "P":
                        return 0
                    if places[t][nr][nc] == "O":
                        for o in range(4):
                            if (nr + dr[o]) < 0 or (nr + dr[o]) >= 5 or (nc + dc[o]) < 0 or (nc + dc[o]) >= 5:
                                continue
                            if visit[nr + dr[o]][nc + dc[o]] == 0:
                                if places[t][nr + dr[o]][nc + dc[o]] == "P":
                                    return 0
            return 1

        result.append(bfs())

    return result