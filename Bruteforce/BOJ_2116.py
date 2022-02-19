N = int(input())
dice = []
for i in range(N):
    x = list(map(int, input().split()))
    dice.append(x)

dict = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

max_num = 0

ans = 0
for i in range(6):
    dice_num = [1,2,3,4,5,6]
    max_side = []
    dice_num.remove(dice[0][i])
    up = dice[0][dict[i]]
    dice_num.remove(up)
    max_side.append(max(dice_num))
    for j in range(1,N):
        dice_num = [1,2,3,4,5,6]
        dice_num.remove(up)
        up = dice[j][dict[dice[j].index(up)]]
        dice_num.remove(up)
        max_side.append(max(dice_num))
    max_side = sum(max_side)
    if ans < max_side :
        ans = max_side

print(ans)