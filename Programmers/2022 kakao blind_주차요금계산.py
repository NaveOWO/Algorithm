import math


def solution(fees, records):
    defaultTime = fees[0]
    defaultFee = fees[1]
    addTime = fees[2]
    addFee = fees[3]

    carDict = {}

    for i in range(len(records)):
        records[i] = records[i].split(' ')
        records[i][0] = records[i][0].split(":")

    records.sort(key=lambda x: int(x[1]))

    if len(records) == 1:
        period = (23 * 60 + 59) - (int(records[0][0][0]) * 60 + int(records[0][0][1]))
        carDict[records[i][1]] = period
    else:
        for i in range(len(records)):
            if records[i][2] == "OUT":
                continue
            if i == len(records) - 1:
                if records[i][2] == "IN":
                    period = (23 * 60 + 59) - (int(records[i][0][0]) * 60 + int(records[i][0][1]))
                    if records[i][1] not in carDict:
                        carDict[records[i][1]] = period
                    else:
                        carDict[records[i][1]] += period
                    continue
            if records[i][1] == records[i + 1][1]:
                period = (int(records[i + 1][0][0]) * 60 + int(records[i + 1][0][1])) - (
                            int(records[i][0][0]) * 60 + int(records[i][0][1]))
                # currentFee = defaultFee + math.ceil((period - defaultTime) / addTime)*addFee
                if records[i][1] not in carDict:
                    carDict[records[i][1]] = period
                else:
                    carDict[records[i][1]] += period
            else:
                period = (23 * 60 + 59) - (int(records[i][0][0]) * 60 + int(records[i][0][1]))
                if records[i][1] not in carDict:
                    carDict[records[i][1]] = period
                else:
                    carDict[records[i][1]] += period
    result = []
    for key in carDict:
        currentFee = defaultFee + math.ceil((carDict[key] - defaultTime) / addTime) * addFee
        if carDict[key] <= defaultTime:
            result.append(defaultFee)
            continue
        result.append(currentFee)

    print(records)

    return result