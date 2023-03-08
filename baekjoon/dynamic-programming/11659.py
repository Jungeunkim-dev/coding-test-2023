N = int(input())
colors = [[0, 0, 0]]

for i in range(N):
    colors.append(list(map(int, input().split())))

d = [[0] * 3 for _ in range(1005)]

d[1][0] = colors[1][0]
d[1][1] = colors[1][1]
d[1][2] = colors[1][2]

for i in range(2, N + 1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + colors[i][0]  # red
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + colors[i][1]  # green
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + colors[i][2]  # blue

print(min(d[N][0], d[N][1], d[N][2]))
