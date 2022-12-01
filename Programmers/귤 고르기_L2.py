def solution(k, tangerine):
    answer = 0
    remainCnt = k
    tempTypeDict = {}
    for i in range(len(tangerine)):
        if tangerine[i] in tempTypeDict:
            tempTypeDict[tangerine[i]] += 1
        else:
            tempTypeDict[tangerine[i]] = 1

    typeList = sorted(tempTypeDict.items(), key=lambda item: item[1], reverse=True)

    for i in range(len(typeList)):
        if remainCnt <= typeList[i][1]:
            answer += 1
            break
        answer += 1
        remainCnt -= typeList[i][1]

    return answer