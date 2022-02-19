from sys import stdin

M,N = map(int, stdin.readline().split())

candy = []
lack = [0]*N

for i in range(N):
    x = int(input())
    candy.append(x)

last = sum(candy) - M
flag = True
while flag == True :
    for i in range(len(candy)):
        if candy[i] > 0:
            candy[i] -= 1
            lack[i] += 1
            last -= 1
            if last == 0:
                flag = False
                break



ans = 0
for i in range(len(lack)):
    ans = ans + lack[i]**2

if ans == 0:
    print(ans)
else:
    print(ans%2**64)

##계속 시간초과 나서 수정중...................................................