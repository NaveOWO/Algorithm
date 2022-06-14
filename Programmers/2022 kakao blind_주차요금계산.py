def solution(fees, records):
    for i in range(len(records)):
        records[i] = records[i].split(' ')
        records[i][0] = records[i][0].split(":")

    records.sort(key=lambda x: int(x[1]))

    entrance = {}
    exit = {}

    for i in range(len(records)):
        if records[i][2] == "IN":
            entrance[records[i][1]] = int(records[i][0][0]) * 60 + int(records[i][0][1])
        else:
            exit[records[i][1]] = int(records[i][0][0]) * 60 + int(records[i][0][1])

    return records