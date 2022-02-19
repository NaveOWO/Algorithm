import collections
q = collections.deque()
N, K = map(int, input().split())
answer = []

for i in range(1, N+1):
    q.append(i)

cnt = 0

# while True :
#     for i in range(N):
#         if q[i] != 0 :
#             if cnt < K-1 :
#                 cnt += 1
#
#             elif cnt == K-1 :
#                 answer.append(q[i])
#                 q[i] = 0
#                 cnt = 0
#     if sum(q) == 0 :
#         break

while  q :
    if cnt < K - 1 :
        q.append(q.popleft())
        cnt += 1
    elif cnt == K-1 :
        answer.append(q.popleft())
        cnt = 0


ans = '<'
for i in range(len(answer)):
    if i == len(answer) -1 :
        ans += str(answer[i]) + '>'
    else :
        ans += str(answer[i]) + ', '

print(ans)
print(answer)




