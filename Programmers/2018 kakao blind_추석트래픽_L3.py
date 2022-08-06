from decimal import Decimal


def solution(lines):
    def getStartPoint(endPoint, duringTime):
        totalEnd = endPoint[0] * 3600 + endPoint[1] * 60 + endPoint[2]
        totalStart = totalEnd - duringTime
        startPoint = []
        for i in range(2):
            startPoint.append(totalStart // (60 ** (2 - i)))
            totalStart = totalStart % (60 ** (2 - i))
        startPoint.append(totalStart)
        return startPoint

    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        lines[i] = lines[i][1:]
        lines[i][0] = lines[i][0].split(':')
        for j in range(3):
            lines[i][0][j] = Decimal(lines[i][0][j])
        lines[i][1] = Decimal(lines[i][1][:-1])
        lines[i].append(getStartPoint(lines[i][0], lines[i][1]))

    startList = []
    for i in range(len(lines)):
        startList.append(lines[i][2][0:2])
    startList.sort(key=lambda x: (x[0], x[1], x[2]))
    endList = []
    for i in range(len(lines)):
        endList.append(lines[i][0][0:2])
    endList.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    startPoint = startList[0]
    endPoint = endList[0]

    timeDict = {}
    currentTime = startPoint
    while True:
        if currentTime == endPoint:
            break
        if currentTime[1] == 59:
            currentTime[0] += 1
            currentTime[1] = 0
        else:
            currentTime[1] += 1
        afterTime = current
        for i in range(len(lines)):
            if currentTime[0]

    print(lines)

    return None