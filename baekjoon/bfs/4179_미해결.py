from collections import deque

R, C = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

fire = [[1002] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
grid = []
result = []  # answer 배열


for i in range(R):
    grid.append(input())

# 불과 지훈이의 최초 위치 설정
for i in range(R):
    for j in range(C):
        if grid[i][j] == "F":
            fire_x, fire_y = i, j
        if grid[i][j] == "J":
            jihoon_x, jihoon_y = i, j

if fire_x == jihoon_x and fire_y == jihoon_y:  # 불의 최초 위치와 지훈이의 위치가 같으면 탈출 불가
    print("IMPOSSIBLE")
    exit(0)


# 불의 확산속도 계산 BFS 함수
def fire_bfs(x, y):
    q = deque()
    q.append((x, y))
    grid[x][y] = "0"
    visited[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= next_x < R and 0 <= next_y < C:
                if grid[next_x][next_y] == "." and not visited[x][y]:
                    q.append((next_x, next_y))
                    grid[next_x][next_y] = grid[cur_x][cur_y] + 1
                    visited[x][y] = True


visited = [[False] * C for _ in range(R)]


# 지훈이의 이동가능 공간 계산 BFS 함수
def jihoon_bfs(x, y):
    q = deque()
    q.append((x, y))
    fire[x][y] = 0
    visited[x][y] = 0
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if 0 <= next_x < R and 0 <= next_y < C:
                if (
                    grid[next_x][next_y] == "."
                    and fire[cur_x][cur_y] + 1 < grid[next_x][next_y]
                ):
                    fire[next_x][next_y] = fire[cur_x][cur_y] + 1
                    visited[next_x][next_y] = True
            else:  # 끝에 다다른 경우에 대해
                return fire[next_x][next_y]
    return 0


fire_bfs(fire_x, fire_y)
jihoon_bfs(jihoon_x, jihoon_y)

# for i in range(R):
#     for j in range(C):
#         if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and fire[i][j] != -1:
#             result.append(fire[i][j])

# if len(result) == 0:
#     print("IMPOSSIBLE")
# else:
#     print(min(result) + 1)
