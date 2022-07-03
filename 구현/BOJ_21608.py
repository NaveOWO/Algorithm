N = int(input())

studentDict = {}
seatList = [[] for i in range(N)]
for i in range(N*N):
    x = list(map(int, input().split()))
    studentDict[x[0]] = x[1:]

def searchCloseSeat():



print(studentDict)