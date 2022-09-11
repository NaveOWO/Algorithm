def solution(survey, choices):
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    total = len(survey)

    def getScore(scoreNum, first, second):
        if scoreNum == 1:
            score[first] += 3
        elif scoreNum == 2:
            score[first] += 2
        elif scoreNum == 3:
            score[first] += 1
        elif scoreNum == 5:
            score[second] += 1
        elif scoreNum == 6:
            score[second] += 2
        elif scoreNum == 7:
            score[second] += 3

    for i in range(total):
        getScore(choices[i], survey[i][0], survey[i][1])
    global result
    result = ""

    def checkScore(x, y):
        global result
        if score[x] > score[y]:
            result += x
        elif score[x] < score[y]:
            result += y
        else:
            result += sorted([x, y])[0]

    checkScore("T", "R")
    checkScore("C", "F")
    checkScore("M", "J")
    checkScore("A", "N")

    return result