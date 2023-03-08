N = int(input())
drink = [0]

# 포도주 값 입력
for i in range(N):
    drink.append(int(input()))


d = [0 for _ in range(10001)]

d[1] = drink[1]
d[2] = d[1] + drink[2]
d[3] = max(d[1], d[2]) + drink[3]

for i in range(4, N + 1):
    d[i] = max(d[i - 3] + d[i - 1], d[i - 2] + d[i])

print(d[N])
