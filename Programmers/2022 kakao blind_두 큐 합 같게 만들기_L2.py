from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    cnt = 0

    while True:
        if sum1 != sum2:
            if sum1 > sum2:
                pointer = q1.popleft()
                q2.append(pointer)
                sum1 -= pointer
                sum2 += pointer
            else:
                pointer = q2.popleft()
                q1.append(pointer)
                sum1 += pointer
                sum2 -= pointer
            cnt += 1
        if sum1 == sum2:
            return cnt
        if cnt == len(queue1) * 4:
            return -1
