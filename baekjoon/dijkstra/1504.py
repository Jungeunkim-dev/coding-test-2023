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


v1_dist = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2_dist = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if v1_dist == INF and v2_dist == INF:
    print(-1)
else:
    print(min(v1_dist, v2_dist))

# 1-> v1 -> v2 -> N
# 1-> v2 -> v1 -> N
# 2경우 중 작은 값을 출력
