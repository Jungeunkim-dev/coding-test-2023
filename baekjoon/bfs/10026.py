from collections import deque

N = int(input())
grid = []
visited = [[False] * N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    grid.append(input())


# 적록색약이 아닌 사람 R, G, B 모두 다르게 취급
def not_bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] == grid[cx][cy]:  # 현재 것과 같은 경우에만
                    visited[nx][ny] = True
                    q.append((nx, ny))


# 적록색약 -> RG, B 로 구분
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[cx][cy] == "B" and grid[nx][ny] == "B":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif (grid[cx][cy] == "R" or grid[cx][cy] == "G") and grid[nx][
                    ny
                ] != "B":
                    visited[nx][ny] = True
                    q.append((nx, ny))


not_cnt = 0
cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            not_bfs(i, j)
            not_cnt += 1


visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(not_cnt, cnt)
