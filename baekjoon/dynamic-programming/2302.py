N = int(input())
M = int(input())
fix = {}  # 고정석 기록

for i in range(M):
    fix[int(input())] = True  # 딕셔너리에 고정석 저장해주기

dp = [0] * (N + 1)

temp = 1

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    if i in fix:
        dp[i] = 1
    elif i - 1 in fix:  # 고정석 바로 다음 좌석이라면 처음부터 경우 세어주기
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

# 각 구간의 곱 구하기

for f in fix:
    temp *= dp[f - 1]
if N not in fix:
    temp *= dp[N]

print(temp)
