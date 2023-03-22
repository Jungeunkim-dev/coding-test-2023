N = int(input())

d = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    d[1][i] = 1  # 자리 1일 경우 가능한 경우는 모두 1

for i in range(2, N + 1):
    for j in range(10):  # 0~9까지의 수
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i - 1][j + 1] + d[i - 1][j - 1]

print(sum(d[N]) % 1000000000)
