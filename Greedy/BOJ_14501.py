from collections import deque

N = int(input())
money = {}
work = {}

for i in range(N):
    x, y = map(int, input().split())
    work[i+1] = i+x
    money[i+1] = y

s_work = sorted(work.items(), key = lambda items: items[1])
arr = deque()
for i in range(len(s_work)):
    arr.append(s_work[i])

day = 0
answer = 0
compare = deque()


point = arr[0][1]

while arr:
    compare = []
    for i in range(len(arr)):
        if arr[0][0] <= day or arr[0][1] > N:
            arr.popleft()
            continue
        else:
            if arr[0][1] == point:
                compare.append(arr.popleft())
            else:
                point = arr[0][1]
                break

    get_money = 0
    for j in range(len(compare)):
        if money[compare[j][0]] > get_money:
            get_money = money[compare[j][0]]
            day = compare[j][1]
    answer += get_money



print(answer)

