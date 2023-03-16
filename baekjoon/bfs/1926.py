from collections import deque

n, m = map(int, input().split())
grid = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    grid.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs 함수

max_area = 0
paint_cnt = 0


def bfs(x, y):
    area = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()
        area += 1
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True
    return area


for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == 1:
            max_area = max(max_area, bfs(i, j))
            paint_cnt += 1

print(paint_cnt)
print(max_area)
