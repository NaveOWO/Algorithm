def solution(s):
    splitedS = s.split(" ")

    result = ""

    for i in range(len(splitedS)):
        if splitedS[i] == "":
            result += " "
            continue
        if type(splitedS[i][0]) == str:
            result += " " + splitedS[i][0].upper() + splitedS[i][1:].lower()
        else:
            result += " " + splitedS[i]

    return result[1:]