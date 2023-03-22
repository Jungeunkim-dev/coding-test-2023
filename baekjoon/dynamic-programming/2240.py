T, W = map(int, input().split())
fall = [0]  # index 1부터 시작하도록 지정
for i in range(T):
    fall.append(int(input()))  # 떨어지는 자두의 시간 기록

dp = [[0] * (W + 1) for _ in range(T + 1)]  # 각 배열의 index 1부터 시작하도록 지정

for i in range(T + 1):  # 0초부터 T초까지
    # 한번도 움직이지 않았을 경우(j=0) 1번에서 떨어지면 기존+1, 2번에서 떨어지면 기존 그대로
    if fall[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    elif fall[i] == 2:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, W + 1):  # 이동 횟수 1회부터 W회까지
        if fall[i] == 2 and j % 2 == 1:  # 이동 횟수=홀수일때(나무2번)
            # 자두는 2번에서 떨어질때 => 자두 +1할 수 있음
            # 이전위치(1)에서 이동할지, 이동안하고 그대로 있을지 비교
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        elif fall[i] == 1 and j % 2 == 0:
            # 자두 1번에서 떨어질 때 => 자두 +1 할 수 있는 경우
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        # 자두 +1 불가한 경우 -> 이전거에서 큰 거 선택
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[T]))
