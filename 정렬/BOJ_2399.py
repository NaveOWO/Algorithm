n = int(input())
x = list(map(int, input().split()))

answer = 0

for i in range(len(x)):
    for j in range(len(x)):
        if i == j:
            continue
        answer += abs(x[i] - x[j])
print(answer)