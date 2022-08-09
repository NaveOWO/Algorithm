from itertools import combinations
N = int(input())

member = [i for i in range(1,N+1)]
status = []
interval = 99999999
for i in range(N):
    status.append(list(map(int, input().split())))

memberCombi = list(combinations(member, N//2))

def getScoreSum(tempList):
    scoreSum = 0
    for combi in tempList:
        r = combi[0]-1
        c = combi[1]-1
        scoreSum += status[r][c] + status[c][r]
    return scoreSum

for i in range(len(memberCombi)//2):
    tempTeam = [memberCombi[i],memberCombi[len(memberCombi)-i-1]]
    startScoreCombi = list(combinations(tempTeam[0], 2))
    startSum = getScoreSum(startScoreCombi)
    linkScoreCombi = list(combinations(tempTeam[1], 2))
    linkSum = getScoreSum(linkScoreCombi)
    interval = min(interval, (abs(startSum - linkSum)))

print(interval)



