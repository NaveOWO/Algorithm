from collections import deque
n = int(input())
numList = list(map(int, input().split()))
x = int(input())
cnt = 0

numList = sorted(numList)
numDict = {}
for number in numList:
    numDict[number] = number

for key in numDict:
    if (x - numDict[key]) in numDict:
        cnt += 1
print(cnt//2)