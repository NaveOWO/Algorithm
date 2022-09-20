def solution(s):
    global removedCnt
    removedCnt = 0
    changedCnt = 0

    def removeZero(currentStr):
        global removedCnt
        resultStr = ''
        for i in range(len(currentStr)):
            if currentStr[i] != '0':
                resultStr += currentStr[i]
            else:
                removedCnt += 1
        return resultStr

    def getBinaryStr(devidedNum):
        result = ''
        while True:
            result += str(devidedNum % 2)
            devidedNum = devidedNum // 2
            if devidedNum < 2:
                result += str(devidedNum)
                break
        return result[::-1]

    while True:
        zeroRemovedStr = len(removeZero(s))
        changedStr = getBinaryStr(zeroRemovedStr)
        changedCnt += 1
        if changedStr == '01':
            answer = [changedCnt, removedCnt]
            break
        s = changedStr
    return answer
