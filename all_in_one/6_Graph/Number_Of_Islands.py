from collections import deque


def NumberOfIslands(grid):
    row = len(grid)
    col = len(grid[0])
    visited = [
        [False] * col for _ in range(row)
    ]  # 처음에 visited = False 배열 만들어줄 때 제대로 짜기 -> IndexOut 에러 뜰수도 있다.

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = True

    def result():
        number_of_islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    number_of_islands += 1
                    bfs(i, j)
        print(number_of_islands)

    result()


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
NumberOfIslands(grid)
