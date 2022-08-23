N, M = map(int, input().split())

office = [[] for _ in range(N)]
for i in range(N):
    office[i] = list(map(int, input().split()))

def numOne():
