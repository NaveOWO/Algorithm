from itertools import combinations

N, S = map(int, input().split())

x = list(map(int, input().split()))

sum_num = []
for i in range(1,len(x)+1):
    sum_num.append(list(combinations(x,i)))

sum_all = []
for i in range(len(sum_num)):
    for j in range(len(sum_num[i])):
        sum_all.append(sum(sum_num[i][j]))

cnt = 0
for i in sum_all:
    if i == S :
        cnt += 1

print(cnt)
