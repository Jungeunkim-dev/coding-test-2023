N = int(input())
dp = [0] * (N + 1)
s = []
max_value = 0

for _ in range(N):
    T, P = map(int, input().split())

    s.append((T, P))

for i in range(N - 1, -1, -1):
    if i + s[i][0] <= N:  # 상담 가능한 범위라면
        dp[i] = max(s[i][1] + dp[s[i][0] + i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
