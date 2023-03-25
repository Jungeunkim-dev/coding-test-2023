from collections import deque

t = int(input())  # 테스트 케이스의 개수
result = []
delta = [(2, 1), (1, 2), (-2, 1), (-2, -1), (2, -1), (-1, 2), (1, -2), (-1, -2)]


def bfs(I, ix, iy, tx, ty):
    visited = [[False] * I for _ in range(I)]
    chess = [[0] * I for _ in range(I)]  # 시작점으로부터 거리를 기록할 배열

    q = deque()  # 현재 위치를 큐에 넣어주기
    q.append((ix, iy))
    visited[ix][iy] = True

    if ix == tx and iy == ty:
        return 0

    while q:
        cx, cy = q.popleft()

        for i in range(8):
            nx, ny = cx + delta[i][0], cy + delta[i][1]

            if 0 <= nx < I and 0 <= ny < I:
                if nx == tx and ny == ty:
                    return chess[cx][cy] + 1

                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    chess[nx][ny] = chess[cx][cy] + 1


for _ in range(t):
    I = int(input())
    ix, iy = map(int, input().split())
    tx, ty = map(int, input().split())
    result.append(bfs(I, ix, iy, tx, ty))

for r in result:
    print(r)
