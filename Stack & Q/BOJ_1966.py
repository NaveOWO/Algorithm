from sys import stdin
from collections import deque
std = stdin.readline


T = int(std())
cnt = 0

for i in range(T) :
    flag = True
    ans = 0
    N, M = map(int, std().split())
    order = deque(map(int, std().split()))
    order_i = deque(0 for _ in range(N))
    order_i[M] = 1
    while True :
        if order[0] == max(order) :
            cnt += 1
            if order_i[0] == 1 :
                print(cnt)
                cnt = 0
                break
            else :
                order.popleft()
                order_i.popleft()
        else :
            order.append(order.popleft())
            order_i.append(order_i.popleft())





