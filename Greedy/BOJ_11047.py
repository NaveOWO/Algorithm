N, K = map(int, input().split())

coin = []
for i in range(N): # 입력받은 동전의 가치를 리스트에 담는다.
    x = int(input())
    coin.append(x)

cnt = 0
for i in range(N-1,-1,-1): # coin리스트를 거꾸로 돌면서
    if K == 0: # 채워야하는 금액이 없으면 Break
        break
    if coin[i] > K : # 채워야하는 금액보다 동전의 가치가 더 크면 넘어가고
        continue
    cnt += K // coin[i] # K를 동전의 가치로 나누어준 몫을 cnt에 더해준다
    K = K % coin[i] # K는 동전의 가치로 나누어준 나머지


print(cnt)