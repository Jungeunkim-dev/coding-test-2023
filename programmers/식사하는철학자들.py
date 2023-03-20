import heapq


def solution(satisfy, k):
    q = []
    visited = [False * len(satisfy)]  # 방문 배열 선언

    for i in range(len(satisfy)):
        heapq.heappush(q, (satisfy[i], i))  # 힙에 넣어주기
    sum = 0
    while k > 0:
        cur = q[0]

        if cur[1] == 0:
            if not visited[cur[1]] and not visited[cur[1] + 1] and not visited[-1]:
                output = heapq.heappop(q)
                sum += output[0]
                visited[output[1]], visited[output[1] + 1], visited[-1] = (
                    True,
                    True,
                    True,
                )
                k -= 1
        elif cur[1] == len(satisfy) - 1:
            if not visited[cur[1]] and not visited[cur[1] - 1] and not visited[0]:
                output = heapq.heappop(q)
                sum += output[0]
                visited[output[1]], visited[output[1] - 1], visited[0] = (
                    True,
                    True,
                    True,
                )
                k -= 1
        else:
            if (
                not visited[cur[1]]
                and not visited[cur[1] - 1]
                and not visited[cur[1] + 1]
            ):
                output = heapq.heappop(q)
                sum += output[0]
                visited[output[1]], visited[output[1] - 1], visited[output[1] + 1] = (
                    True,
                    True,
                    True,
                )
                k -= 1

    print(sum)


solution([5, 4, 4, 6, 2, 1, 3], 3)
