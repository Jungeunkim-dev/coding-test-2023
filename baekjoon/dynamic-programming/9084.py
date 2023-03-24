T = int(input())
result = []

for i in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)  # 다이나믹 테이블 저장 결과

    dp[0] = 1

    for c in coin:
        for j in range(M + 1):
            if j >= c:
                dp[j] += dp[j - c]

    # for j in range(M + 1):
    #     for c in coin:  # 가지고 있는 동전의 값들에 대해
    #         if j >= c:  # 만약에 해당 값보다 크면
    #             dp[j] += dp[j - c]  # 해당 값으로 넘어뛸 수 있는 이전 값의 값을 더해준다 (경우의수)

    result.append(dp[M])

for r in result:
    print(r)
