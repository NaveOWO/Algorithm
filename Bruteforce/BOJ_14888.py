from itertools import permutations

N = int(input())
numList = list(map(int, input().split()))
operatorCount = list(map(int, input().split()))
operatorList = []
for cnt in range(len(operatorCount)):
    for i in range(operatorCount[cnt]):
        if cnt == 0:
            operatorList.append('+')
            continue
        if cnt == 1:
            operatorList.append('-')
            continue
        if cnt == 2:
            operatorList.append('*')
            continue
        operatorList.append('/')

operatorRotateList = list(permutations(operatorList,len(operatorList)))

resultList=  [0 for i in range(len(operatorRotateList))]

def getResult(i, numList, currentOperatorList):
    for j in range(1,len(numList)):
        if currentOperatorList[j-1] == '+':
            resultList[i] += numList[j]
            continue
        if currentOperatorList[j-1] == '-':
            resultList[i] -= numList[j]
            continue
        if currentOperatorList[j-1] == '*':
            resultList[i] *= numList[j]
            continue
        if resultList[i] < 0:
            resultList[i] = (abs(resultList[i]) // numList[j]) * -1
        else:
            resultList[i] = resultList[i]//numList[j]



for i in range(len(operatorRotateList)):
    resultList[i] += numList[0]
    getResult(i,numList,operatorRotateList[i])


print(max(resultList), min(resultList), sep='\n')