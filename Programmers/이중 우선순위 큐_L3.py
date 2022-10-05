import heapq
from collections import deque


def solution(operations):
    ORDER = len(operations)
    q = []

    for i in range(ORDER):
        operations[i] = operations[i].split(' ')
        operations[i][1] = int(operations[i][1])

    for order in operations:
        if order[0] == 'I':
            heapq.heappush(q, order[1])
            continue
        if len(q) == 0:
            continue
        if order[1] == 1:
            tempQ = []
            for i in range(len(q) - 1):
                tempQ.append(heapq.heappop(q))
            q = tempQ
        else:
            heapq.heappop(q)

    if len(q) == 0:
        return [0, 0]

    q.sort()

    return [q[-1], q[0]]