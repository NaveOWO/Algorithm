from collections import deque
n, m = map(int, input().split())

computer = [[0 for i in range(n+1)] for j in range(n+1)]
efficiency = [0 for i in range(n+1)]
trust = deque()

for i in range(m):
    x, y = map(int, input().split())
    computer[y][x] = 1

def bfs():
    while trust:
        x, y = trust.popleft()
        for i in range(1,n+1):
            if computer[y][i] == 1:
                trust.append((y,i))
                efficiency[x] += 1
                print(efficiency,i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if computer[i][j] == 1:
            efficiency[i] += 1
            trust.append((i,j))
            bfs()

max_num = max(efficiency)
answer = []
for i in range(1,len(efficiency)):
    if efficiency[i] == max_num:
        answer.append(i)

answer.sort()
for num in answer:
    print(num, end = ' ')

print(efficiency)