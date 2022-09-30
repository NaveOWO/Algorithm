def solution(info, query):
    APPLICANTS = len(info)
    CONDITIONS = len(query)

    dictCombi = {"cpp": {"backend": {"junior": {"pizza": {}, "chicken": {}}, "senior": {"pizza": {}, "chicken": {}}},
                         "frontend": {"junior": {"pizza": {}, "chicken": {}}, "senior": {"pizza": {}, "chicken": {}}}},
                 "java": {"backend": {"junior": {"pizza": {}, "chicken": {}}, "senior": {"pizza": {}, "chicken": {}}},
                          "frontend": {"junior": {"pizza": {}, "chicken": {}}, "senior": {"pizza": {}, "chicken": {}}}},
                 "python": {"backend": {"junior": {"pizza": {}, "chicken": {}}, "senior": {"pizza": {}, "chicken": {}}},
                            "frontend": {"junior": {"pizza": {}, "chicken": {}},
                                         "senior": {"pizza": {}, "chicken": {}}}}}

    answer = [0 for i in range(CONDITIONS)]

    for i in range(len(info)):
        info[i] = info[i].split(' ')

    for i in range(len(query)):
        query[i] = query[i].split(' ')

    for i in range(len(info)):
        if info[i][4] not in dictCombi[info[i][0]][info[i][1]][info[i][2]][info[i][3]]:
            dictCombi[info[i][0]][info[i][1]][info[i][2]][info[i][3]][info[i][4]] = 1
        else:
            dictCombi[info[i][0]][info[i][1]][info[i][2]][info[i][3]][info[i][4]] += 1

    splitedQuery = []
    for i in range(len(query)):
        splitedQuery.append([])
        for j in range(len(query[i])):
            if query[i][j] != 'and':
                splitedQuery[-1].append(query[i][j])

    def getCorrectApplicant(condition):
        cnt = 0
        result = []
        if condition[0] == '-':
            condition[0] = ['cpp', 'java', 'python']
        else:
            condition[0] = [condition[0]]
        if condition[1] == '-':
            condition[1] = ['frontend', 'backend']
        else:
            condition[1] = [condition[1]]
        if condition[2] == '-':
            condition[2] = ['junior', 'senior']
        else:
            condition[2] = [condition[2]]
        if condition[3] == '-':
            condition[3] = ['chicken', 'pizza']
        else:
            condition[3] = [condition[3]]
        for lan in condition[0]:
            for job in condition[1]:
                for his in condition[2]:
                    for food in condition[3]:
                        for sco in dictCombi[lan][job][his][food]:
                            if int(sco) >= int(condition[4]):
                                cnt += dictCombi[lan][job][his][food][sco]
        return cnt

    for i in range(len(splitedQuery)):
        answer[i] += getCorrectApplicant(splitedQuery[i])

    return answer