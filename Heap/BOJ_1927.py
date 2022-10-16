import heapq, sys
n = int(sys.stdin.readline())
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
        print(heapq.heappop(heapList))
        length -= 1
        return
    heapq.heappush(heapList, num)
    length += 1
for i in range(n):
    getResult(int(sys.stdin.readline()))
