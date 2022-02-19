from sys import stdin
import heapq
std = stdin.readline

N = int(std())
array = []

for i in range(N):
    array.append(int(std()))

heap = []

for i in range(len(array)) :
    if array[i] != 0 :
        heapq.heappush(heap, -array[i])
    else :
        if heap :
            print(heapq.heappop(heap) * -1)

        else :
            print(0)




