import heapq

N,T = map(int, input().split())
card = []

card = list(map(int, input().split()))
heapq.heapify(card)

for j in range(T):
    pick = 0
    for i in range(2):
        pick += heapq.heappop(card)
    for i in range(2):
        heapq.heappush(card, pick)

print(sum(card))

