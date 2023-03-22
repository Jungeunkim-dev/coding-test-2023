N = int(input())
drink = [0]

# 포도주 값 입력
for i in range(N):
    drink.append(int(input()))

d = [0 for _ in range(N + 1)]  # dp 배열 선언

if N == 1:
    print(drink[1])
elif N == 2:
    print(drink[1] + drink[2])
else:
    d[1] = drink[1]
    d[2] = drink[1] + drink[2]

    for i in range(3, N + 1):
        d[i] = max(d[i - 2] + drink[i], d[i - 3] + drink[i - 1] + drink[i], d[i - 1])

    print(d[N])
