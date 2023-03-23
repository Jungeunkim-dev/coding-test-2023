n = int(input())
tri = [[0]]  # idx 편의를 위해 1부터 시작하도록 설정
# dp = [0] * (501)  # 1부터 500까지 각 칸의 최대값 저장
dp = [[0]]

for i in range(n):  # 삼각형 배열을 추가시켜 준다.
    tri.append(list(map(int, input().split())))
    dp.append([0] * (i + 1))


if n == 1:
    print(tri[1][0])
elif n == 2:
    print(tri[1][0] + max(tri[2][0], tri[2][1]))
else:
    dp[1][0] = tri[1][0]  # 삼각형 맨 위의 원소
    dp[2][0] = tri[1][0] + tri[2][0]  # 2번째 단계의 원소
    dp[2][1] = tri[1][0] + tri[2][1]

    answer = dp[1][0] + max(dp[2])  # max val of each step, return answer

    for i in range(3, n + 1):
        # 각 단계의 원소 중 최대 경로의 값을 구하기
        for j in range(i):  # 각 단계의 원소의 수 == 단계수
            # 해당 줄의 1, last 원소면 바로 위 원소의 값을 물려받는다.
            if j == 0:  # 첫 번째 원소일때
                dp[i][j] = dp[i - 1][0] + tri[i][j]
            elif j == len(tri[i]) - 1:  # 해당 단계의 마지막 원소일때
                dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
            else:  # 이외의 배열 요소일때
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

        answer = max(dp[i])  # 해당 칸의 최대값

    print(answer)
