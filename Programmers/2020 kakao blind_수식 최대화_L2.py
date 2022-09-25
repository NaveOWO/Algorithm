import re


def solution(expression):
    operator = ['*', '+', '-']
    currentOp = []
    combi = {3: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]], 2: [[0, 1], [1, 0]]}
    global splitedExpression
    splitedExpression = re.split('([-|+|*])', expression)
    answer = 0

    def getSingleResult(prevNum, sign, nextNum):
        if sign == '*':
            return prevNum * nextNum
        if sign == '+':
            return prevNum + NextNum
        if sign == '-':
            return prevNum - NextNum

    def getTotalResult(signs):
        global splitedExpression
        i = 0
        while True:
            sign = signs[2]
            tempStr = []
            for i in range(len(splitedExpression)):
                if i != 0 and splitedExpression[i - 1] == sign:
                    continue
                if expression[i] == sign:
                    result = getSingleResult(int(splitedExpression[i - 1]), splitedExpression[i],
                                             int(splitedExpression[i + 1]))
                    tempStr.pop()
                    tempStr.append(result)
                    continue
                tempStr.append(splitedExpression[i])
            if i == len(signs) - 1:
                break
            i += 1
            splitedExpression = tempStr

    for letter in splitedExpression:
        if letter in operator and letter not in currentOp:
            currentOp.append(letter)
    term = len(currentOp)

    for i in range(len(combi[term])):
        answer = max(answer, abs(getTotalResult(combi[term][i])))

    return splitedExpression