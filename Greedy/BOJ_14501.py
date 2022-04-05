from collections import deque

N = int(input())
money = deque()
work = deque()

for i in range(N):
    x, y = map(int, input().split())
    work[i+1] = i+x
    money[i+1] = y

s_work = sorted(work.items(), key = lambda items: items[1])










print(s_work)