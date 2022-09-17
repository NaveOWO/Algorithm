def solution(s):
    def checkIndex(index):
        if index % 2 == 1:
            return "lower"
        return "upper"

    result = ""

    wordList = s.split(" ")

    for j in range(len(wordList)):
        print(wordList[j], j)
        if wordList[j] == "":
            if j != len(wordList) - 1:
                result += " "
            continue
        for i in range(len(wordList[j])):
            if checkIndex(i) == "lower":
                result += wordList[j][i].lower()
            else:
                result += wordList[j][i].upper()
            if j != len(wordList) - 1 and i == len(wordList[j]) - 1:
                result += " "

    return result