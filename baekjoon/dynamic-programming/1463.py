N = int(input())

d = [0 for _ in range(1000005)]  # 10^6 까지 가능해야 하니까 -> 필요한 공간 초기화

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1  # 기본
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[N])  # 어차피 N까지 가니까 굳이 for 문 안에서 if i==N인지 비교 안해줘도 됨.
