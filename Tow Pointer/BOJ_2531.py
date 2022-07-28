from collections import deque
import collections

n, d, k, c = map(int, input().split())
cnt = 0

fishBelt = []
for i in range(n):
    fishBelt.append(int(input()))

for i in range(k-1):
    fishBelt.append(fishBelt[i])

colaboDict = collections.defaultdict(int)
for fish in range(1,d+1):
    colaboDict[fish]

totalDish = len(fishBelt)
fishCollaboration = deque(fishBelt[0:k])

for fish in fishCollaboration:
    colaboDict[fish] += 1

for i in range(k,totalDish):
    tempCnt = 0
    colaboDict[fishCollaboration[0]] -= 1
    fishCollaboration.popleft()
    fishCollaboration.append(fishBelt[i])
    colaboDict[fishBelt[i]] += 1
    for key in colaboDict:
        if colaboDict[key] > 0:
            tempCnt += 1
    if colaboDict[c] == 0 :
        tempCnt += 1
    cnt = max(cnt, tempCnt)

print(cnt)
