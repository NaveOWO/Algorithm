import sys, heapq
N = int(sys.stdin.readline())
global heapList
global length

heapList = []
length = 0

def getResult(num):
    global heapList
    global length
    if num == 0:
        if length == 0:
            print(0)
            return
        print(heapq.heappop(heapList)[1])
        length -= 1
        return
    heapq.heappush(heapList, (abs(num), num))
    length += 1


for i in range(N):
    getResult(int(sys.stdin.readline()))