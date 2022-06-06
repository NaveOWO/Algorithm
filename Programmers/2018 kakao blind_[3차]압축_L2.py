from string import ascii_uppercase


def solution(msg):
    result = []
    wordDict = {}
    for i in range(len(ascii_uppercase)):
        wordDict[ascii_uppercase[i]] = i + 1

    cnt = 26
    startIndex = 0
    for i in range(len(msg)):
        checkStr = msg[i]
        printStr = msg[i]
        if i == startIndex:
            if i == len(msg) - 1:
                result.append(wordDict[checkStr])
                break
            # if i == len(msg)-2:
            #     result.append(wordDict[msg[i]+msg[i+1]])
            #     break
            for j in range(i + 1, len(msg)):
                checkStr += msg[j]
                if checkStr not in wordDict:
                    wordDict[checkStr] = cnt + 1
                    cnt += 1
                    startIndex = j
                    result.append(wordDict[printStr])
                    break
                printStr += msg[j]
                if j == len(msg) - 1:
                    result.append(wordDict[printStr])

    return result