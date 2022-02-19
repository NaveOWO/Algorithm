N = int(input())

conference = []
for i in range(N):
    conference.append(list(map(int,input().split())))

conference.sort(key = lambda x : (x[1],x[0]))

cnt = 0
last = conference[0][1]
for i in range(len(conference)):
    if i == 0:
        cnt += 1
        last = conference[i][1]
    else:
        if conference[i][0] >= last:
            cnt += 1
            last = conference[i][1]
print(cnt)