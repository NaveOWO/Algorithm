from itertools import permutations


def solution(relation):
    cnt = 0
    seperatedList = [[] for i in range(len(relation[0]))]

    for i in range(len(relation)):
        for j in range(len(relation[i])):
            seperatedList[j].append(relation[i][j])

    for i in range(len(seperatedList)):
        if len(seperatedList[i]) == len(set(seperatedList[i])):
            cnt += 1
            for j in range(len(relation)):
                del relation[j][i]

    rotateList = [i for i in range(len(relation[0]))]

    return rotateList