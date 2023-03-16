from collections import deque
from collections import Counter

M, N = map(int, input().split())
grid = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# visited = [] visited가 있어야 할까?

for i in range(N):
    grid.append(list(map(int, input().split())))

q = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            q.append((i, j))


def rippen():  # 그냥 매번 전체 배열을 검사해야 하는 건가? visited 생각 안해도 되고?
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            n_x, n_y = cur_x + dx[i], cur_y + dy[i]

            if n_x >= 0 and n_x < N and n_y >= 0 and n_y < M:
                if grid[n_x][n_y] == 0:
                    # 익음 처리
                    grid[n_x][n_y] = grid[cur_x][cur_y] + 1
                    q.append((n_x, n_y))


rippen()

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(grid[i]))

print(cnt - 1)
