import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


def topological_sort():
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        print(cur, end=" ")

        for v in graph[cur]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)


topological_sort()
