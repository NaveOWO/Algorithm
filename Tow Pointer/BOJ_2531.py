from collections import deque

n, d, k, c = map(int, input().split())
cnt = 0

fishBelt = []
for i in range(n):
    fishBelt.append(int(input()))

for i in range(k-1):
    fishBelt.append(fishBelt[i])

totalDish = len(fishBelt)
fishCollaboration = deque(fishBelt[0:k])
for i in range(k,totalDish):
    fishCollaboration.popleft()
    fishCollaboration.append(fishBelt[i])
