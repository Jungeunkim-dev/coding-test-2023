import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
result = []

for i in range(K):
    lines.append(int(input()))


def max_length(start, end):
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in range(K):
            cnt += lines[i] // mid

        if cnt < N:
            end = mid - 1
        if cnt >= N:
            start = mid + 1
    print(end)  # end를 리턴하는 이유 이해하기 -> '최대' 길이를 구하는 것이기 때문


max_length(1, max(lines))
