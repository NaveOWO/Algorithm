import math

def solution(n, k):
    global createdNumber, cnt
    createdNumber = ''
    cnt = 0

    def createNewNumber(originNum):
        global createdNumber
        while True:
            createdNumber += str(originNum % k)
            originNum = originNum // k
            if originNum <= k:
                createdNumber += str(originNum)
                break
        createdNumber = createdNumber[::-1]
        print("new:", createdNumber)
        getCheckList(createdNumber)

    def checkPrimeNum(target):
        global cnt
        for i in range(2, int(math.sqrt(target)) + 1):
            if target % i == 0:
                return cnt
        cnt += 1
        print(target)
        return cnt

    def getCheckList(changedNum):
        if len(changedNum) == 1:
            if checkPrimeNum(int(changedNum)) == True:
                cnt += 1
                return cnt
            return 0
        checkList = changedNum.split('0')
        for number in checkList:
            if number == '' or number == '1':
                continue
            checkPrimeNum(int(number))

    createNewNumber(n)
    return cnt