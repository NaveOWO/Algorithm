N = int(input())
array = []
home = []
for i in range(N):
    array.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if array[x][y] == 1:
        cnt +=1
        array[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

cnt = 0
result = 0

for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            home.append(cnt)
            result +=1
            cnt = 0

home.sort()
print(result)
for i in range(len(home)):
    print(home[i])