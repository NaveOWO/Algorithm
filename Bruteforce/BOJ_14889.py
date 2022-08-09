from itertools import combinations
N = int(input())

member = [i for i in range(1,N+1)]
status = []
for i in range(N):
    status.append(list(map(int, input().split())))

memberCombi = list(combinations(member, N//2))
print(memberCombi)

for i in range(len(memberCombi)//2):
    temp = [memberCombi[i],memberCombi[len(memberCombi)-i-1]]
    print(temp)
# for combi in memberCombi:
#     start = combi[0:N//2]
#     link = combi[N//2:]
#     print(start, link)
