def solution(expression):
    seperated = []
    for i in range(len(expression)):
        if i == 0:
            seperated.append(expression[i])
        else:
            if expression[i].isdigit() == True:
                if expression[i-1].isdigit() == True:
                    seperated[-1] += expression[i]
                else:
                    seperated.append(expression[i])
            else:
                seperated.append(expression[i])
    return seperated