T = int(input())

dp = [0] * 1000001
result = []

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for _ in range(T):
    result.append(dp[int(input())])

for r in result:
    print(r)
