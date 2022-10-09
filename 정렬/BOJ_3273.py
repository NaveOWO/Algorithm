n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
answer = 0

numDict = {}
for i in range(len(numbers)):
    if numbers[i] not in numDict:
        numDict[numbers[i]] = 1
        continue
    numDict[numbers[i]] += 1

for i in range(len(numbers)):
    if x-numbers[i] in numDict:
        answer += numDict[numbers[i]]


print(answer//2)