spot = list(input())
N = int(input())
second = []

for i in range(N) :
    order = []
    order = input().split()
    if order[0] == 'L' :
        if spot :
            second.append(spot.pop())
        else :
            continue
    if order[0] == 'D' :
        if second :
            spot.append(second.pop())
        else :
            continue
    if order[0] == 'B' :
        if spot :
            spot.pop()
        else :
            continue
    if order[0] == 'P' :
        spot.append(order[-1])

while second :
    spot.append(second.pop())

answer = ''.join(spot)

print(answer)

