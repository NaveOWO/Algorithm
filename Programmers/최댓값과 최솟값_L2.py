def solution(s):
    sList = s.split(' ')
    intList = []
    for string in sList:
        intList.append(int(string))

    result = [min(intList), max(intList)]
    strResult = ""
    strResult += str(result[0]) + " " + str(result[1])

    return strResult