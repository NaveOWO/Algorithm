def solution(files):
    fileList = [['', '', '', i] for i in range(len(files))]
    HEAD, NUMBER, TAIL = 0, 1, 2

    for i in range(len(files)):
        pointer = HEAD
        loweredFile = files[i].lower()
        for j in range(len(loweredFile)):
            if loweredFile[j].isdigit() and pointer == HEAD:
                pointer = NUMBER
                fileList[i][pointer] += (loweredFile[j])
                continue

            if loweredFile[j].isdigit() == False and pointer == NUMBER:
                pointer = TAIL
                fileList[i][pointer] += (loweredFile[j])
                continue

            fileList[i][pointer] += (loweredFile[j])
        fileList[i][1] = int(fileList[i][1])

    fileList.sort(key=lambda x: (x[0], x[1]))

    result = []
    for i in range(len(fileList)):
        result.append(files[fileList[i][3]])

    return result