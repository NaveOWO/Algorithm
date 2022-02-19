N = int(input())
big = []
score = [0]*N
cnt = 0

for i in range(N):
    x, y = map(int, input().split())
    big.append([x,y])

for i in range(N):
    for j in range(N):
        if i != j :
            for var in range(2):
                if big[i][var] < big[j][var]:
                    cnt += 1
            if cnt == 2:
                score[i] += 1
                cnt = 0
            else:
                cnt = 0
for i in range(N):
    print(score[i]+1, end = ' ')
