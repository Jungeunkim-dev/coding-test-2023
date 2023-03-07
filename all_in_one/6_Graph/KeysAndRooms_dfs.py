def canVisitAllRooms(rooms):
    # 방문 여부 처리 배열 선언
    visited = []

    def dfs(v):
        for room in rooms[v]:
            if room not in visited:
                visited.append(room)
                dfs(room)

    dfs(0)
    return False not in visited


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))
