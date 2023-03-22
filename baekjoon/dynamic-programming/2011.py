code = "0" + input()
dp = [0] * (len(code) + 1)

if code[1] == "0":
    print(0)  # 암호 생성이 불가능한 경우
else:
    dp[0] = 1
    dp[1] = 1  # 첫번째 자리는 무조건 1

    for i in range(2, len(code)):
        if code[i] > "0":
            dp[i] += dp[i - 1]

        if code[i - 1] != "0" and code[i - 1] + code[i] < "27":
            dp[i] += dp[i - 2]

    print(dp[len(code) - 1] % 1000000)
