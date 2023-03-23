N = int(input())
M = int(input())
fix = {}  # 고정석 기록 (오름차순이므로 정렬 필요X)

for i in range(M):
    fix[int(input())] = True  # 딕셔너리에 고정석 저장해주기

dp = [0] * (N + 1)

temp = 1

dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

# 각 구간의 길이별로 업데이트 해주기

st = 1

if not fix:  # 고정석이 없는 경우
    print(dp[N])
else:  # 고정석이 1개 이상 있는 경우
    for f in fix:
        temp *= dp[f - st]
        st = f + 1
    temp*=dp[]
    print(temp)
