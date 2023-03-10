import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

    return distance[end]
