from itertools import permutations


def solution(expression):
    global originStr
    operators = []
    answer = 0
    for letter in expression:
        if letter.isdigit() == False and letter not in operators:
            operators.append(letter)

    combis = list(permutations(operators, len(operators)))

    def splitExpression(originExpression):
        result = [[]]
        for letter in originExpression:
            if letter.isdigit() == True:
                result[-1].append(letter)
            else:
                result.append([])
                result[-1].append(letter)
                result.append([])
        for i in range(len(result)):
            result[i] = ''.join(result[i])
        return result

    originStr = splitExpression(expression)

    def culculate(sign, x, y):
        if sign == '+':
            return x + y
        if sign == '-':
            return x - y
        if sign == '*':
            return str(x * y)

    def getParticularResult(sign):
        global originStr
        tempStr = []
        for i in range(len(originStr)):
            if originStr[i] == sign:
                result = culculate(sign, int(tempStr.pop()), int(originStr[i + 1]))
                tempStr.append(result)
                continue
            if i != 0 and originStr[i - 1] == sign:
                continue
            tempStr.append(originStr[i])
        originStr = tempStr

    for i in range(len(combis)):
        currentOrder = combis[i]
        originStr = splitExpression(expression)
        for operator in currentOrder:
            getParticularResult(operator)
        answer = max(answer, abs(int(originStr[0])))
    return answer+1