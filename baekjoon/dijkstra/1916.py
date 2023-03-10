import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)


for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))


dijkstra(start)
print(distance[end])

# 문제 풀 때 배열이름, 기존 변수명 겹치지 않도록 하자
