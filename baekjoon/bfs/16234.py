from collections import deque

N, L, R = map(int, input().split())

people = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N):
    people.append(list(map(int, input().split())))

move = 0  # 인구 이동 횟수


# 가능한 만큼 '연합'을 확장시켜 나간다
def bfs(i, j):
    union = []  # 연합인 경우
    union_sum = 0

    q = deque()
    visited[i][j] = True
    q.append((i, j))
    union.append((i, j))
    union_sum += people[i][j]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:  # 범위 내부에 있을 때
                if (
                    L <= abs(people[cx][cy] - people[nx][ny]) <= R
                    and not visited[nx][ny]
                ):  # 차이가 L 이상 R 이하라면
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))
                    union_sum += people[nx][ny]

    # 연합의 경우를 변경시켜 준다.
    for u in union:
        people[u[0]][u[1]] = (union_sum) // len(union)  # 연합의 개수를 업데이트해준다.

    return len(union) - 1  # 연합(인구 이동 여부)


while True:
    visited = [[False] * N for _ in range(N)]
    stop = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                stop += bfs(i, j)

    if stop == 0:  # 더 이상 변화가 없으면
        print(move)
        break

    move += 1
