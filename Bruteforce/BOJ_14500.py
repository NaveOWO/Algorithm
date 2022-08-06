N, M = map(int, input().split())

paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r,c):

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr => N or nr < 0 or nc => M or nc < 0:
            continue
        cnt += 1
        if cnt < 4:
            dfs(nr, nc)
