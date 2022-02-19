n ,k = map(int, input().split()) # n,k 입력

number = [] # 동전의 가치를 담을 리스트
for i in range(n):
    number.append(int(input()))

dp = [0 for _ in range(k+1)] # 합이 0부터 k까지의 경우의 수를 담을 dp리스트
dp[0] = 1 # 합이 0인 경우는 아무것도 선택 안하는 1가지

for i in number: # 사용할 동전의 가치를 순회한다
    for j in range(i,k+1): # 사용할 동전으로 만들 수 있는 합
        dp[j] = dp[j] + dp[j-i] 
print(dp[k])