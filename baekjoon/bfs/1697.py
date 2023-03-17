from collections import deque

N, K = map(int, input().split())
data = [-1 for _ in range(100001)]


def subin():
    q = deque()
    q.append(N)
    data[N] = 0
    while data[K] == -1:
        cur = q.popleft()

        for next in [cur + 1, cur - 1, cur * 2]:
            if 0 <= next <= 100000 and data[next] == -1:
                data[next] = data[cur] + 1
                q.append(next)

    print(data[K])


subin()
