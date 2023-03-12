import sys
from collections import deque

input = sys.stdin.readline

T = int(input())  # testcases

for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())

    # topological sort
    q = deque()
    time_sum = 0  # 건설에 걸리는 시간 누적합

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        time_sum += time[cur - 1]

        for v in graph[cur]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    print(time_sum)
