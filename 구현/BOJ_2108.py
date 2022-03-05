N = int(input())
region = []
ma = 0
mi = 101
for i in range(N):
    x = list(map(int, input().split()))
    if max(x) > ma:
        ma = max(x)
    if min(x) > mi:
        mi = min(x)
    region.append(x)

print(region , ma , mi)

