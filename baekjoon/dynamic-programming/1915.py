grid = []

n, m = map(int, input().split())
max_area = 0

for _ in range(n):
    s = input()
    grid.append(list(map(int, list(s))))


for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and grid[i][j] == 1:
            grid[i][j] = min(grid[i][j - 1], grid[i - 1][j], grid[i - 1][j - 1]) + 1
        max_area = max(max_area, grid[i][j])

print(max_area * max_area)
