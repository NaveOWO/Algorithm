def solution(data, col, row_begin, row_end):
    colIndex = col - 1
    start = row_begin - 1
    end = row_end - 1

    data.sort(key=lambda x: (x[colIndex], -x[0]))

    hashs = []

    for i in range(start, end + 1):
        sumMod = 0
        for j in range(len(data[i])):
            sumMod += data[i][j] % (i + 1)
        hashs.append(sumMod)

    answer = 0
    for i in range(len(hashs)):
        if i == 0:
            answer = hashs[i]
            continue
        answer = (answer ^ hashs[i])

    return answer