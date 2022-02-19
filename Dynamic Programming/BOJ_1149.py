n = int(input())

paint = []
for i in range(n):
    paint.append(list(map(int, input().split())))

for j in range(1,n):
    paint[j][0] = paint[j][0] + min(paint[j - 1][1],paint[j - 1][2])
    paint[j][1] = paint[j][1] + min(paint[j - 1][0], paint[j - 1][2])
    paint[j][2] = paint[j][2] + min(paint[j - 1][1], paint[j - 1][0])

print(min(paint[n-1]))
