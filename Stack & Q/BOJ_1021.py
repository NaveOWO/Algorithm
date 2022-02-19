from collections import deque
N, M = map(int, input().split())

allOfNum = deque(i for i in range(1,N+1))
num = deque((map(int, input().split())))

cnt = 0

for i in range(M):
    if num[i] == allOfNum[0]:
        allOfNum.popleft()
    else:
        while True :
            if allOfNum.index(num[i]) <= len(allOfNum)//2:
                allOfNum.append(allOfNum.popleft())
                cnt += 1
            else:
                allOfNum.appendleft(allOfNum.pop())
                cnt += 1
            if allOfNum[0] == num[i]:
                allOfNum.popleft()
                break


print(cnt)