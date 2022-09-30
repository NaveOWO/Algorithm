from collections import deque


def solution(n):
    def getBinaryNum(num):
        binaryList = deque()
        cnt = 0
        while True:
            binaryList.appendleft(str(num % 2))
            if num % 2 == 1:
                cnt += 1
            num = num // 2
            if num < 2:
                binaryList.appendleft(str(num))
                cnt += 1
                break
        return cnt

    originCnt = getBinaryNum(n)
    testNum = n + 1
    answer = -1

    while True:
        if getBinaryNum(testNum) == originCnt:
            answer = testNum
            break
        else:
            testNum += 1

    return answer