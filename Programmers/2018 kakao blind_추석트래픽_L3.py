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

    timeDict = {}
    for i in range(lines):
        for j in range(lines[i][1]):

    print(lines)

    return 0