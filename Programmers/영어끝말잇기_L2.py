def solution(n, words):
    isTold = {}
    individualCnt = {}
    for i in range(1, n + 1):
        individualCnt[i] = 0

    cnt = 0
    round = 1

    for i in range(len(words)):
        if (words[i] in isTold) or (i != 0 and words[i - 1][-1] != words[i][0]):
            if (i + 1) % n != 0:
                return [(i + 1) % n, round]
            else:
                return [n, round]
        isTold[words[i]] = "yes"
        cnt += 1
        if cnt == n:
            cnt = 0
            round += 1
            print(round)
        if (i + 1) % n == 0:
            individualCnt[n] += 1
        else:
            individualCnt[(i + 1) % n] += 1

    return [0, 0]