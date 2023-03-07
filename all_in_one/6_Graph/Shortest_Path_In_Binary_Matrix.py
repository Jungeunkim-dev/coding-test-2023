from collections import deque


def shortestPath(grid):
    visited = [[False] * len(grid) for _ in range(len(grid[0]))]

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def bfs(x, y):
        q = deque()
        q.append((x, y, 0))
        visited[x][y] = True

        while q:
            cur_x, cur_y, depth = q.popleft()

            if cur_x == 2 and cur_y == 2:
                return depth

            for i in range(8):
                next_x = cur_x + direction[i][0]
                next_y = cur_y + direction[i][1]

                if next_x >= 0 and next_x < 3 and next_y >= 0 and next_y < 3:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        q.append((next_x, next_y, depth + 1))
                        visited[next_x][next_y] = True

    return bfs(0, 0)


print(shortestPath([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
