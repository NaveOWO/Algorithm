import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    hq = []
    answer = 0

    for work in works:
        heapq.heappush(hq, [-1*work, work])

    for _ in range(n):
        a, b = heapq.heappop(hq)
        heapq.heappush(hq, [a+1, b-1])

    while hq:
        lst = heapq.heappop(hq)
        answer += lst[1] ** 2

    return answer

