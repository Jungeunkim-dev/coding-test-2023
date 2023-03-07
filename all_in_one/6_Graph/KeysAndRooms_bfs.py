from collections import deque


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True

        while q:
            cur = q.popleft()
            for room in rooms[cur]:
                if not visited[room]:
                    q.append(room)
                    visited[room] = True

    bfs(0)

    return visited


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))
