N = int(input())

nation = list(map(int, input().split()))

M = int(input())

if sum(nation) <= M :
    print(max(nation))
else:
    nation.sort()
    flag = True
    pin = True
    left = nation[0]
    right = nation[-1]
    answer = 0
    while flag == True :
        money = 0
        mid = (left + right)//2
        for i in range(len(nation)):
            if nation[i] <= mid :
                money += nation[i]
            else :
                money += mid
        if money == M :
            answer = mid
            break
        elif money > M :
            right = mid
            if pin == False :
                flag = False
        else :
            left = mid
            answer = mid
            pin = False




    print(answer)
