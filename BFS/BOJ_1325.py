import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

computer = [[] for i in range(n+1)]
efficiency = [0 for i in range(n+1)]

def bfs(start):
    cnt = 1
    trust = deque()
    trust.append(start)
    visit = [0 for i in range(n + 1)]
    visit[start] = 1
    while trust:
        x = trust.popleft()
        for i in computer[x]:
            if visit[i] == 0:
                trust.append(i)
                cnt += 1
                visit[i] = 1
    efficiency[start] = cnt
    return cnt

for i in range(1,m+1):
    x, y = map(int, input().split())
    computer[y].append(x)

answer = [0 for i in range(n+1)]
for i in range(1,n+1):
    bfs(i)
    answer[i] = bfs(i)

for i in range(1,n+1):
    if answer[i] == max(answer):
        print(i, end = ' ')