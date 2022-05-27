def solution(info, query):
    result = [0 for i in range(len(query))]

    # info 분리하기
    infoDic = {'language': [], 'category': [], 'history': [], 'food': [], 'score': []}
    for i in range(len(info)):
        info[i] = info[i].split(' ')
        for j in range(len(info[i])):
            if j == 0:
                infoDic['language'].append(info[i][j])
            elif j == 1:
                infoDic['category'].append(info[i][j])
            elif j == 2:
                infoDic['history'].append(info[i][j])
            elif j == 3:
                infoDic['food'].append(info[i][j])
            else:
                infoDic['score'].append(info[i][j])

    # query 분리해서 requestList 라는 새로운 리스트생성
    requestList = [[] for i in range(len(query))]
    for i in range(len(query)):
        query[i] = query[i].split(' ')
        for j in range(len(query[i])):
            if query[i][j] != 'and':
                requestList[i].append(query[i][j])

    requestDic = {'language': [], 'category': [], 'history': [], 'food': [], 'score': []}
    for i in range(len(requestList)):
        for j in range(len(requestList[i])):
            if j == 0:
                requestDic['language'].append(requestList[i][j])
            elif j == 1:
                requestDic['category'].append(requestList[i][j])
            elif j == 2:
                requestDic['history'].append(requestList[i][j])
            elif j == 3:
                requestDic['food'].append(requestList[i][j])
            else:
                requestDic['score'].append(requestList[i][j])

    def validate(i, j):
        for key in requestDic:
            if requestDic[key][i] == '-':
                continue
            if key == 'score':
                if int(requestDic[key][i]) <= int(infoDic[key][j]):
                    continue
            if requestDic[key][i] != infoDic[key][j]:
                return
        result[i] += 1
        return

    for i in range(len(query)):
        for j in range(len(infoDic)):
            validate(i, j)

    return result