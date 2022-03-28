N = int(input())
student = list(map(int, input().split()))
main, sub = map(int, input().split())

answer = 0
for i in range(len(student)):
    student[i] -= main
    answer += 1
    if student[i] > 0:
        if student[i] % sub == 0:
            answer += (student[i]//sub)
        else:
            answer += (student[i]//sub) +1

print(answer)