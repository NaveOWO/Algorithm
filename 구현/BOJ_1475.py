roomNum = int(input())

roomNum = str(roomNum)

numDict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

cnt = 0
for num in roomNum:
    if num == '9':
        numDict['6'] += 1
        continue
    numDict[num] += 1

for key in numDict:
    cnt = max(cnt, numDict[key])

if list(numDict.values()).count(max(numDict.values())) == 1 and numDict['6'] == cnt:
    if cnt % 2 == 0:
        answer = cnt//2
    else:
        answer = cnt//2 +1
else:
    answer = cnt


print(answer)